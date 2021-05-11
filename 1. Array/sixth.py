def duplicate_string(s):
    my_set = set([])

    write_stream = 0
    read_stream = 0

    while read_stream < len(s):
        if s[read_stream] not in my_set:
            my_set.add(s[read_stream])
            s[write_stream] = s[read_stream]
            write_stream += 1
        read_stream += 1

    s[write_stream] = '\0'

new = "my anme is chadscon"
duplicate_string(new)