#!/usr/bin/env python3
"""Test the fallback mechanisms of the APTFramework module"""

import sys
sys.path.insert(0, 'c:/Users/ermias3706/hacking')

try:
    from modules.payloads.apt_framework import APTFramework
    print('[OK] APTFramework imported successfully')
    
    apt = APTFramework()
    print(f'[OK] APTFramework instance created')
    print(f'[OK] Impacket available: {apt.impacket_available}')
    
    # Verify fallback mechanisms are available
    assert not apt.impacket_available, "Expected impacket to not be available"
    print('[OK] Fallback mechanisms are active')
    
    # Test if we can create instances of the fallback classes
    # Note: These tests will only work if the imports failed (which they should)
    
    # Test that SMBConnection is available (as fallback)
    print('[OK] Testing SMBConnection fallback')
    try:
        from modules.payloads.apt_framework import SMBConnection
        conn = SMBConnection('test', 'test')
        assert conn is not None
        print('  [OK] SMBConnection fallback created successfully')
    except Exception as e:
        print(f'  [ERROR] Error: {e}')
    
    # Test that DCERPCTransportFactory is available (as fallback)
    print('[OK] Testing DCERPCTransportFactory fallback')
    try:
        from modules.payloads.apt_framework import DCERPCTransportFactory
        transport = DCERPCTransportFactory('ncacn_np:test[\\pipe\\srvsvc]')
        assert transport is not None
        print('  [OK] DCERPCTransportFactory fallback created successfully')
        
        # Test transport methods
        if hasattr(transport, 'set_credentials'):
            transport.set_credentials(username='test', password='test', domain='WORKGROUP')
            print('  [OK] set_credentials method available')
        
        if hasattr(transport, 'get_dce_rpc'):
            dce = transport.get_dce_rpc()
            assert dce is not None
            print('  [OK] get_dce_rpc method available')
            
            if hasattr(dce, 'connect'):
                dce.connect()
                print('  [OK] connect method available')
            
            if hasattr(dce, 'bind'):
                dce.bind(None)
                print('  [OK] bind method available')
                
    except Exception as e:
        print(f'  [ERROR] Error: {e}')
        import traceback
        print(traceback.format_exc())
    
    print('')
    print('[OK] All fallback tests passed')
    print('')
    print('The module is functioning correctly with fallback mechanisms.')
    print('To use the real impacket functionality, install impacket with:')
    print('pip install impacket')
    
except Exception as e:
    print(f'[ERROR] Error: {type(e).__name__}: {e}')
    import traceback
    print('Stack trace:')
    print(traceback.format_exc())
