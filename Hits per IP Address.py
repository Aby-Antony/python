def CalculateApacheIpHits(logfile.txt):
    # Make a dictionary to store IP addresses and their hit counts
    # and read the contents of the log file line by line
    IpHitListing = {}
    Contents = open("logfile.txt", "r").xreadlines(  )
    # You can use .readlines in old Python, but if the log is huge...

    # Go through each line of the logfile
    for line in Contents:
        # Split the string to isolate the IP address
        Ip = line.split(" ")[0]

        # Ensure length of the IP address is proper (see discussion)
        if 6 < len(Ip) <= 15:
            # Increase by 1 if IP exists; else set hit count = 1
            IpHitListing[Ip] = IpHitListing.get(Ip, 0) + 1

    return IpHitListing