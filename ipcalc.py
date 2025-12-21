import ipaddress
import sys

def get_network_info(network):
    """Calculates and prints basic network information."""
    # Determine IPv4 or IPv6 max prefix length
    max_prefixlen = network.max_prefixlen
    
    # Calculate host bits and block size
    host_bits = max_prefixlen - network.prefixlen
    block_size = 2**host_bits 
    
    print("\n=== IP Network Information ===")
    print(f"IP Version: IPv{network.version}")
    
    # Network, Broadcast, and Mask details are only relevant for IPv4 or networks >= /127 in IPv6
    if network.version == 4:
        print(f"Network Address: {network.network_address}")
        print(f"Broadcast Address: {network.broadcast_address}")
        print(f"Subnet Mask: {network.netmask}")
        print(f"Wildcard Mask: {network.hostmask}")
        print(f"Number of Usable Hosts: {network.num_addresses - 2 if network.num_addresses > 2 else 0}")
        
        # --- NEW FEATURE: Calculate Number of Subnets Relative to Classful Network ---
        try:
            first_octet = int(str(network.network_address).split('.')[0])
            
            # Determine Classful boundary
            if 1 <= first_octet <= 126:
                classful_prefix = 8  # Class A
            elif 128 <= first_octet <= 191:
                classful_prefix = 16 # Class B
            elif 192 <= first_octet <= 223:
                classful_prefix = 24 # Class C
            else:
                # Default for special ranges (e.g., 0.0.0.0/0 or 240.x.x.x) or when classful concept doesn't apply cleanly
                classful_prefix = network.prefixlen
            
            subnetwork_bits = network.prefixlen - classful_prefix

            if subnetwork_bits > 0:
                num_blocks = 2**subnetwork_bits
                print(f"Total Blocks Available (relative to Classful /{classful_prefix}): {num_blocks}")
            elif subnetwork_bits == 0:
                 print(f"Total Blocks Available (relative to Classful /{classful_prefix}): 1 (This is the Classful Network itself)")
            else:
                print(f"Note: This prefix is a Supernet (prefix < /{classful_prefix})")

        except Exception as e:
            # Fallback in case of unexpected address format issues (should be rare)
            print(f"Warning: Could not calculate classful block count. Error: {e}")

    elif network.version == 6:
        print(f"Network Range Start: {network.network_address}")
        print(f"Network Range End: {network.broadcast_address}")
        # Note: Broadcast/Netmask concepts are different/absent in IPv6 
        # but the range start/end and address count are key.
        print(f"Number of Usable Hosts: {network.num_addresses}")
        # Note: Classful concepts do not apply to IPv6.

    print(f"Prefix Length: /{network.prefixlen}")
    print(f"Block Size / Total Addresses: {block_size}")
    
    return block_size
      
def ip_calculator():
    """
    Handles user input and orchestrates the IP calculation in a continuous loop.
    """
    print("Welcome to the Enhanced IP Calculator! Enter 'exit' to quit at any time.")

    while True:
        # --- Combined Input IP and Prefix ---
        ip_prefix_input = input("\nEnter IP address and Prefix (e.g., 192.168.1.50/24 or 2001::/64): ")
        
        # Check for exit command
        if ip_prefix_input.lower() == 'exit':
            print("Exiting IP Calculator. Goodbye!")
            sys.exit(0)

        try:
            # ipaddress.ip_network handles the combined IP/prefix input directly.
            # strict=False allows host bits to be set (i.e., you can enter 192.168.1.50/24)
            network = ipaddress.ip_network(ip_prefix_input, strict=False)
            
            # Call the function to display the information
            get_network_info(network)
            
        except ValueError as e:
            # Catch errors for invalid format or IP address
            print(f"Error: Invalid input format or address. {e}")
            continue

if __name__ == "__main__":
    ip_calculator()