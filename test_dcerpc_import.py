#!/usr/bin/env python3
import sys
sys.path.insert(0, 'c:/Users/ermias3706/hacking')

# Test importing from modules.payloads.apt_framework
try:
    from modules.payloads.apt_framework import DCERPCTransportFactory
    print("DCERPCTransportFactory imported successfully")
    
    # Test creating an instance
    try:
        transport = DCERPCTransportFactory('ncacn_np:test[\\pipe\\srvsvc]')
        print(f"DCERPCTransportFactory instance created: {type(transport)}")
        
        # Test methods
        if hasattr(transport, 'set_credentials'):
            transport.set_credentials(username='test', password='test', domain='WORKGROUP')
            print("set_credentials method available")
            
        if hasattr(transport, 'get_dce_rpc'):
            dce = transport.get_dce_rpc()
            print(f"get_dce_rpc method available: {type(dce)}")
            
    except Exception as e:
        print(f"Error creating DCERPCTransportFactory instance: {e}")
        import traceback
        print(traceback.format_exc())
        
except Exception as e:
    print(f"Error importing DCERPCTransportFactory: {e}")
    import traceback
    print(traceback.format_exc())
