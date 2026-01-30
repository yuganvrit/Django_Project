# import dns.resolver
# import smtplib
# import socks
# import socket
# import requests

# # NetNut Credentials
# # Use the standard global SOCKS5 gateway for reliability
# SOCKS_HOST = "gw.netnut.net" 
# SOCKS_PORT = 9595 # SMTP MUST use 9595
# PROXY_USER = "Vrittechnologies-res-any"
# PROXY_PASS = "Kj03iX67qIVcVi8"

# # HTTP format for the initial validation check
# HTTP_PROXY_URL = f"http://{PROXY_USER}:{PROXY_PASS}@gw.netnut.net:5959"
# http_proxies = {
#     "http": HTTP_PROXY_URL,
#     "https": HTTP_PROXY_URL,
# }

# def validate_proxy():
#     try:
#         # Use a simple timeout to check if the HTTP proxy responds
#         response = requests.get("https://api.ipify.org?format=json", proxies=http_proxies, timeout=10)
#         print(f"✅ Proxy Connection Successful. IP: {response.json()['ip']}")
#         return True
#     except Exception as e:
#         print(f"❌ Proxy Validation Failed: {e}")
#         return False

# def check_email_existence(target_email):
#     domain = target_email.split('@')[-1]
    
#     try:
#         # 1. DNS Resolution (Do this BEFORE switching to SOCKS mode)
#         print(f"🔍 Finding MX records for {domain}...")
#         mx_records = dns.resolver.resolve(domain, 'MX')
#         mx_host = str(sorted(mx_records, key=lambda r: r.preference)[0].exchange).rstrip('.')
#         mx_ip = str(dns.resolver.resolve(mx_host, 'A')[0])
#         print(f"📍 Mail Server: {mx_host} ({mx_ip})")

#         # 2. Switch to SOCKS5 for the raw TCP connection
#         socks.set_default_proxy(
#             socks.SOCKS5, 
#             SOCKS_HOST, 
#             SOCKS_PORT, 
#             username=PROXY_USER, 
#             password=PROXY_PASS
#         )
#         socket.socket = socks.socksocket

#         # 3. SMTP Handshake
#         print(f"🚀 Connecting to {mx_ip} via SOCKS5 (Port {SOCKS_PORT})...")
#         server = smtplib.SMTP(timeout=20)
#         server.set_debuglevel(1) 
        
#         # Connect to the mail server on Port 25
#         server.connect(mx_ip, 25)
#         server.helo("vrit-tech.com")
#         server.mail('verify@vrit-tech.com')
        
#         # 4. The RCPT TO Check
#         code, message = server.rcpt(target_email)
#         server.quit()

#         if code == 250:
#             return True, f"✅ {target_email} exists."
#         elif code == 550:
#             return False, f"❌ {target_email} does not exist."
#         else:
#             return None, f"⚠️ Server response {code}: {message}"

#     except Exception as e:
#         return None, f"🔥 SMTP Error: {str(e)}"

# # --- Run ---
# if validate_proxy():
#     email_to_test = "iamyugdashaudi@gmail.com"
#     exists, result = check_email_existence(email_to_test)
#     print(f"\n--- FINAL RESULT ---")
#     print(result)

