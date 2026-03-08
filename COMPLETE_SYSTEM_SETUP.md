# Social C2 System - Complete Setup and Usage Guide

## 🎯 System Overview

This comprehensive Social C2 (Command and Control) system is designed for ethical hacking and penetration testing on social media platforms. It provides a complete framework for managing attack campaigns, deploying payloads, and monitoring results in real-time.

## 📊 System Components

### 1. **C2 Server** (Port 5000)
- RESTful API backend
- Session management
- Payload deployment and tracking
- Database storage for credentials and session data

### 2. **Dashboard** (Port 3000)
- Real-time web interface
- Session and payload monitoring
- Quick action buttons for common attacks
- Statistics and activity logging

### 3. **Phishing Server** (Port 8000)
- Simple HTTP server
- Serves phishing pages and payload files
- Directory listing for easy access to resources

### 4. **Auto-Pentest Campaign** (Background Process)
- Automated attack chain execution
- Continuous monitoring of targets
- Integration with C2 server

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Flask and Flask-CORS libraries
- Access to social media APIs (for certain modules)

### Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Start all services (Windows)
deploy_full_stack.bat

# Start all services (Linux/macOS)
chmod +x deploy_full_stack.sh
./deploy_full_stack.sh
```

### Access the Dashboard
Open your browser and navigate to: **http://localhost:3000**

## 🎮 Usage Instructions

### Dashboard Features

#### Session Management
- **View Active Sessions**: See all ongoing attack sessions
- **End Sessions**: Terminate active sessions
- **Create Sessions**: Start new attack campaigns

#### Payload Deployment
- **Reconnaissance**: Gather information about targets
- **Credential Harvesting**: Deploy phishing attacks
- **Exploitation**: Exploit vulnerabilities

#### Statistics
- Total sessions and active sessions counter
- Payloads deployed and success rate
- Real-time activity logging

### API Usage Examples

#### Get System Health
```bash
curl -X GET http://localhost:5000/health
```

#### Create Session
```bash
curl -X POST http://localhost:5000/sessions \
  -H "Content-Type: application/json" \
  -d '{
    "target": "testuser",
    "platform": "instagram"
  }'
```

#### Deploy Payload
```bash
curl -X POST http://localhost:5000/payloads \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": 1,
    "payload_type": "recon",
    "target": "testuser"
  }'
```

## 🔧 Configuration

### Database
The system uses SQLite for data storage. The database file `c2.db` is automatically created and managed by the C2 server.

### Logs
Logs are stored in the `logs/` directory (created automatically if it doesn't exist). Each log file contains detailed information about sessions, payload deployments, and system events.

### Payloads
Payloads are stored in the `modules/payloads/` directory. You can create custom payloads and they will be automatically available through the dashboard and API.

## 🛡️ Security Considerations

### Ethical Usage
This tool is for educational and ethical hacking purposes only. Unauthorized use against systems you don't own or have explicit permission to test is illegal and unethical.

### Legal Compliance
- Ensure you have proper authorization before conducting any penetration testing
- Follow local laws and regulations regarding cybersecurity
- Respect privacy laws and regulations

### System Hardening
- Restrict access to the C2 server
- Use strong authentication
- Encrypt sensitive data
- Regularly update and patch the system

## 📈 System Statistics

### Current Status (as of installation)
- **C2 Server**: Running (Status: ok)
- **Dashboard**: Running (Status: 200)
- **Phishing Server**: Running (Status: 200)
- **Active Sessions**: 1 (Target: testuser1, Platform: Instagram)
- **Deployed Payloads**: 2 (Recon and Credential Harvest)

## 🔍 Troubleshooting

### Common Issues

#### Port Conflicts
If ports 5000, 3000, or 8000 are already in use:
```bash
# Check what's using the port (Windows)
netstat -ano | findstr :5000

# Terminate conflicting process (Windows)
taskkill /F /PID <PID>
```

#### Service Not Starting
- Check Python installation and dependencies
- Verify all required files are present
- Check log files for error messages

#### API Errors
- Verify the C2 server is running
- Check database connectivity
- Verify request formats are correct

## 📚 Resources

### Documentation
- **README.md**: Detailed usage instructions
- **DEPLOYMENT_SUMMARY.md**: System deployment details
- **test_api.py**: API testing script
- **system_overview.py**: System status check
- **templates/dashboard.html**: Web interface source

### Modules
- **modules/recon.py**: Reconnaissance module
- **modules/cred_harvest.py**: Credential harvesting module
- **modules/session_hijack.py**: Session hijacking module
- **modules/exploit.py**: Exploitation module
- **modules/persistence.py**: Persistence module
- **modules/mass_checker.py**: Mass vulnerability checker

## 🔄 Updates and Maintenance

### Updating the System
```bash
# Stop current services
taskkill /F /IM python.exe

# Pull latest changes
git pull

# Restart services
python c2_server.py &
python dashboard.py &
python -m http.server 8000 &
python auto_pentest.py &
```

### Database Backup
```bash
# Create backup
cp c2.db c2.db.backup

# Restore from backup
cp c2.db.backup c2.db
```

### Log Rotation
Logs are automatically rotated based on size. Older log files are compressed and stored in the `logs/archives/` directory.

## 📞 Support

If you encounter any issues or have questions:
1. Check the log files in the `logs/` directory
2. Use the system overview script to diagnose problems: `python system_overview.py`
3. Run the API test script: `python test_api.py`
4. Review the installation instructions in this guide

## 🌐 Community

- **GitHub Repository**: [Link to repository]
- **Issue Tracker**: [Link to issues]
- **Documentation**: [Link to docs]
- **Discord/Slack**: [Community channels]

---

**Remember: This tool is for ethical hacking purposes only. Always obtain proper authorization before conducting any penetration testing activities.**
