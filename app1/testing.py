import socks
import ssl
import dns.resolver

def recv(sock):
    return sock.recv(4096).decode(errors="ignore").strip()

def send(sock, cmd):
    sock.sendall((cmd + "\r\n").encode())
    return recv(sock)


def get_primary_mx(domain):
    """
    Returns the single highest-priority MX host
    """
    answers = dns.resolver.resolve(domain, "MX")

    # pick MX with lowest preference value
    mx = min(answers, key=lambda r: r.preference)
    return str(mx.exchange).rstrip(".")

def smtp_mx_check(target_email):
    try:
        proxy_host = "gw-open.netnut.net"
        proxy_port = 9595
        proxy_user = "Vrittechnologies-evsh-np"
        proxy_pass = "Kj03iX67qIVcVi8"

        domain = target_email.split("@")[1]
        mx_host = get_primary_mx(domain)

        s = socks.socksocket()
        s.settimeout(20)
        s.set_proxy(
            socks.SOCKS5,
            proxy_host,
            proxy_port,
            True,
            proxy_user,
            proxy_pass
        )

        print("Connecting to Google MX (port 25)...")
        s.connect((mx_host, 25))
        print("S:", recv(s))

        # EHLO
        print("S:", send(s, "EHLO example.com"))

        # STARTTLS (optional but supported)
        print("S:", send(s, "STARTTLS"))
        context = ssl.create_default_context()
        s = context.wrap_socket(s, server_hostname=mx_host)

        # EHLO again
        print("S:", send(s, "EHLO example.com"))

        # MAIL / RCPT (policy check only)
        print("S:", send(s, "MAIL FROM:<test@example.com>"))
        response = send(s, f"RCPT TO:<{target_email}>")
        print(f"S (Result for {target_email}): {response}")

        if response.startswith("250"):
            print("SMTP routing accepted (NOT existence confirmation)")
        elif response.startswith("550"):
            print("Rejected by policy")
        else:
            print("SMTP response received")

        send(s, "QUIT")
        s.close()

    except Exception as e:
        print("Error:", e)


# RUN
smtp_mx_check("afoad25@amazon.co.jp")
