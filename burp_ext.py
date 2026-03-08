#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Burp Suite Extension - Custom Extension Template
This extension provides basic functionality for Burp Suite
"""

# Burp Suite imports (only available when running inside Burp Suite)
try:
    from burp import IBurpExtender
    from burp import ITab
    from javax.swing import JPanel, JLabel
    from java.awt import BorderLayout
    BURP_AVAILABLE = True
except ImportError:
    # Create dummy classes/interfaces for development/testing purposes
    class IBurpExtender:
        pass
    
    class ITab:
        pass
    
    class JPanel:
        def __init__(self):
            self.layout = None
        def setLayout(self, layout):
            self.layout = layout
        def add(self, component, constraints):
            pass
    
    class JLabel:
        def __init__(self, text):
            self.text = text
    
    class BorderLayout:
        CENTER = "center"
    
    BURP_AVAILABLE = False

class BurpExtender(IBurpExtender, ITab):
    """
    Main Burp Extension class that implements IBurpExtender and ITab
    """
    
    def registerExtenderCallbacks(self, callbacks):
        """
        Required method for IBurpExtender - called when extension is loaded
        """
        # Keep a reference to our callbacks object
        self._callbacks = callbacks
        
        # Set our extension name
        self._callbacks.setExtensionName("Custom Burp Extension")
        
        # Obtain an instance of the Burp helper object
        self._helpers = callbacks.getHelpers()
        
        # Create our UI components
        self._panel = JPanel()
        self._panel.setLayout(BorderLayout())
        
        # Add a label to the panel
        label = JLabel("Custom Burp Extension Loaded Successfully!")
        self._panel.add(label, BorderLayout.CENTER)
        
        # Register ourselves as a custom tab
        callbacks.addSuiteTab(self)
        
        print("Custom Burp Extension loaded successfully!")
        
    def getTabCaption(self):
        """
        Required method for ITab - returns the tab name
        """
        return "Custom Extension"
        
    def getUiComponent(self):
        """
        Required method for ITab - returns the UI component
        """
        return self._panel

if __name__ == "__main__":
    # This is not required for Burp Suite integration
    print("This is a Burp Suite extension. It should be loaded within Burp Suite.")
    
    if not BURP_AVAILABLE:
        print("\nNote: Running outside of Burp Suite environment.")
        print("Dummy implementations are being used for testing purposes.")
        print("\nTesting extension structure...")
        try:
            extender = BurpExtender()
            print("BurpExtender instance created successfully")
            
            required_methods = ['registerExtenderCallbacks', 'getTabCaption', 'getUiComponent']
            for method in required_methods:
                if hasattr(extender, method):
                    print(f"BurpExtender has {method} method")
                else:
                    print(f"BurpExtender missing {method} method")
            
            print("\nExtension structure is valid!")
            
        except Exception as e:
            print(f"Error testing extension: {e}")
