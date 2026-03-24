import dolphin_memory_engine as dme

def setup():
    #Unlock Badges
    hops = 0
    offset = 12
    while hops <= 40:
        level=0x906A8F77+(hops*offset)
        dme.write_byte(level, 0x03)
        hops+=1

    #Watch Cutscenes
    #Refer to GitHub for more info
    #
    #Cutscenes (Also known as 'Flicks')
    ### Even though we unlock every cutscene
    ### the game will always play the cutscene if
    ### you entered the level with a status of 0x02
    dme.write_byte(0x906A962B, 0x03)
    dme.write_byte(0x906A9637, 0x03)
    dme.write_byte(0x906A9643, 0x03)
    dme.write_byte(0x906A964F, 0x03)
    dme.write_byte(0x906A965B, 0x03)
    dme.write_byte(0x906A9667, 0x03)
    dme.write_byte(0x906A9673, 0x03)
    dme.write_byte(0x906A967F, 0x03)
    dme.write_byte(0x906A968B, 0x03)

    #Dialogs
    dme.write_byte(0x906A96F7, 0x03)
    dme.write_byte(0x906A973F, 0x03)
    dme.write_byte(0x906A971B, 0x03)
    dme.write_byte(0x906A96EB, 0x03)

    #Unlock Map (0x10) Unlock Magic Sock (0x14) Unlock shop doors (0xFF)
    dme.write_byte(0x906A7007, 0xFF)

    #Give apartment an owner
    #(To unlock only Kirby's pad do x00 x82)
    #(For everything to xFF xFF)
    dme.write_bytes(0x906A7005, b"\x00\x82")

    #Unlock shops
    dme.write_byte(0x906A7002, 0x01) #Show merchants

    #Unlock all boss doors + patch castle
    dme.write_byte(0x906A7067 + (0 * 36), 0x03)
    dme.write_byte(0x906A7067 + (43 * 36), 0x03)
    dme.write_byte(0x906A7067 + (44 * 36), 0x03)
    dme.write_byte(0x906A7067 + (45 * 36), 0x03)
    dme.write_byte(0x906A7067 + (46 * 36), 0x03)
    dme.write_byte(0x906A7067 + (47 * 36), 0x03)
    dme.write_byte(0x906A7067 + (48 * 36), 0x03)
