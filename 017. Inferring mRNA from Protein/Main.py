# Given: A protein string of length at most 1000 aa.
#
# Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000.
#         (Don't neglect the importance of the stop codon in protein translation.)

protein = "MARLSGHMNYEACTKHGWEWNQWKVTKSQIFWMQRGSRDPVDNINKNHLSGPEHMMILPQLCMVKFPTFEFQEFIANVFDNNTIVGRLLSILRVQQGWNFDCFNWMKRSVVCFSSAWWIHFSTWTFCSYWFIWLCAGDKYPYAEVFGRHPELCKDMMCHCIEKSPKANSRGFHEDTFGDFSVLAWNASEVHENWTLWGLNIDGLEYCSACKGQWRRGHKDTHPACPLEGHKYWHSKLSGKRWCKDHAWDIMSTEAGDKFGNAVVQATFDAYRKIACRRDKRSKNLDNRPLSICFWDLNNKWPWGKCKWAHINIGSEIVMDRALDNEYDPPSPFAGSVFLHAPRVCEVEPGHGFDKADPGHHGKTKCVEAWCRTAHIINHKIWDSVHVVDLPYTHPRFHLLLQDARMVPGDAADSTCKMYYQTSFTSTDCNNVWHASNQHVSSSIKASLVQVTGPKSPGLQLHATKRISIDLQWCHEDCIVVAFETIKEKHAFMTHDSNTLPHCMSNESMAQSIWTDRPIGCVGNTETCTHDPYHGNNCKCCHQNDHQWKSQHEQDFFCNHADRASGHCTVSNIAVDHEALRACVMDVRQIQLCTEGHGEKPCRPFMLMACFFAQIGWMVRVNREMDYWCYYLTLIITCVEMTGTHQSAIKFWVAQYMIMNRMPSHNVLPRPMVEWGRYTNYQPSGWLGHTMKEGFCWFHDCQRGPMAQNPYFCLPTKMPCYDMQIFPRNKGCAKAGNYWRGNMYYPKSMSRETETTYVRHITTCPIQNVDCVGRAVGMNFMHDLEHMGAWMLLEGKYMIYEKDLAQMCCQVGHYVAQCNFEYSIRPWGSIHTLESHEWTNVHCGIKRTRWFSYQMCDREYCQSLCYPICDNRDHTAERQWVRVGNRRTHSEKYIVMTWMSVYIIWPKVWNKAIGDTIHFTQKLFWKAAYNKFNWCGVCQNSYGWYGWLVDVKTLNTSSFHQWNHAMHPMIHKYRYRQQWYVWSHSEDAHHPLAPPTF"

table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
inv_table = {}
for k,v in table.items():
    inv_table[v]=inv_table.setdefault(v,[])
    inv_table[v].append(k)

count = 1
for i in protein:
    count *= len(inv_table[i])
print((count*3)%1000000)
