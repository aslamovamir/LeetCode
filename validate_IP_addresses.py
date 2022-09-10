# Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address 
# or "Neither" if IP is not a correct IP of any type.

# A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading 
# zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses while "192.168.01.1", "192.168.1.00",
# and "192.168@1.1" are invalid IPv4 addresses.

# A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

# 1 <= xi.length <= 4
# xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
# Leading zeros are allowed in xi.
# For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, 
# while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.

 

# Example 1:

# Input: queryIP = "172.16.254.1"
# Output: "IPv4"
# Explanation: This is a valid IPv4 address, return "IPv4".
# Example 2:

# Input: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
# Output: "IPv6"
# Explanation: This is a valid IPv6 address, return "IPv6".
# Example 3:

# Input: queryIP = "256.256.256.256"
# Output: "Neither"
# Explanation: This is neither a IPv4 address nor a IPv6 address.

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        # let's first assume that the query is IPv4
        sequence = queryIP.split('.')
        print(sequence)
        if len(sequence) == 4:
            invalid = False
            # if the list not null, it is IPv4, whether valid or not
            # now loop through each sequence and check if each is a number and no leading zeroes
            for item in sequence:
                try:
                    component = int(item)
                    if component < 0 or component > 255:
                        invalid = True
                        break
                except:
                    invalid = True
                    break
                if item[0] == '0' and len(item) != 1:
                    invalid = True
                    break
            if not invalid:
                return "IPv4"
        # now let's assume that it is IPv6
        sequence = queryIP.split(':')
        print(sequence)
        if len(sequence) == 8:
            # if the list not null, it is IPv6, whether valid or not
            for item in sequence:
                # check length
                if len(item) < 1 or len(item) > 4:
                    return "Neither"
                try:
                    item = int(item,16)
                except:
                    return "Neither"
            return "IPv6"
        else:
            return "Neither"
          
