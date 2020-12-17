class Solution:
    """
    Part 1
    """
    def countInvalidTickets(self, rules: [str], ticket: [int], other_tickets: [[str]]) -> int:
        map = []
        for r in rules:
            values = r[r.index(":")+1:]
            first, second = values.split(" or ")
            x, y = first.split("-")
            x2, y2 = second.split("-")

            map.append([ [int(x), int(y)], [int(x2), int(y2)] ])
        # e.g
        # 0:[[1, 3], [5, 7]]
        # 1:[[6, 11], [33, 44]]
        # 2:[[13, 40], [45, 50]]
        qty = 0
        invalidTickets = []
        for i, ticket in enumerate(other_tickets):
            for val in ticket:
                val = int(val)
                valid = False
                for ruleset in map:
                    if ( val >= ruleset[0][0] and val <= ruleset[0][1] ) or ( val >= ruleset[1][0] and val <= ruleset[1][1] ):
                        valid = True
                        break
                if not valid:        
                    qty += val
                    invalidTickets.append(i)
                    break
        return qty, invalidTickets

    def matchFields(self, rules: [str], allTickets: [[str]]) -> int:
        map = []
        for r in rules:
            values = r[r.index(":")+1:]
            first, second = values.split(" or ")
            x, y = first.split("-")
            x2, y2 = second.split("-")
            map.append([ [int(x), int(y)], [int(x2), int(y2)] ])
        
        # pra cada regra
        posRules = {}

        # itera sobre todos os campos de todos os tickets pra achar quais regras são válidas a ele
        for n in range(len(allTickets[0])):
            for i, ruleset in enumerate(map[:]):
                valid = True
                for ticket in allTickets:
                    val = int(ticket[n])
                    if not (( val >= ruleset[0][0] and val <= ruleset[0][1] ) or ( val >= ruleset[1][0] and val <= ruleset[1][1] )):
                        valid = False
                        break
                if valid:
                    if n not in posRules:
                        posRules[n] = []
                    posRules[n].append(i)

        # encontradas as regras de cada campo, remove um a um as que tem só 1 campo possivel
        positions = []
        rulesSet = 20
        while rulesSet > 0:
            for i, x in posRules.items():
                if len(x) == 1:
                    if x[0] < 6:
                        positions.append(i)
                    rulesSet -= 1
                    item = x[0]
                    for p in posRules.values():
                        if item in p:
                            p.remove(item)
                    break

        res = 1
        for x in positions:
            res *= int(allTickets[0][x])
        return res

rules = """departure location: 26-724 or 743-964
departure station: 33-845 or 864-954
departure platform: 26-472 or 482-967
departure track: 27-140 or 158-956
departure date: 25-884 or 894-952
departure time: 37-924 or 941-949
arrival location: 48-311 or 335-972
arrival station: 39-703 or 724-950
arrival platform: 40-108 or 114-950
arrival track: 30-101 or 108-967
class: 33-386 or 399-949
duration: 44-444 or 452-956
price: 27-220 or 234-974
route: 42-774 or 790-959
row: 48-900 or 918-956
seat: 42-165 or 178-949
train: 45-831 or 842-965
type: 49-522 or 548-974
wagon: 32-565 or 588-964
zone: 27-608 or 617-953"""
ticket = [101,71,193,97,131,179,73,53,79,67,181,89,191,137,163,83,139,127,59,61]
other_ticket = """818,269,901,814,631,821,607,127,247,636,755,762,559,670,189,249,499,273,565,463
470,472,597,259,345,370,827,520,595,92,204,52,104,248,688,500,99,694,659,803
432,251,666,518,217,469,791,304,139,724,516,522,702,496,804,142,408,518,82,823
333,471,429,58,129,754,304,879,459,288,268,386,217,138,284,554,762,370,769,161
242,255,344,634,710,124,813,241,697,342,600,637,202,421,75,195,496,470,806,554
464,948,755,334,662,493,251,948,286,472,562,400,774,790,385,263,100,689,681,83
511,796,756,593,637,647,377,277,178,642,588,695,591,495,678,682,346,318,417,84
762,238,803,343,290,80,558,216,806,157,821,359,654,661,870,552,503,604,200,754
613,290,370,761,595,899,743,868,289,162,303,653,810,311,95,468,588,456,772,342
352,332,559,813,443,243,881,75,522,245,190,61,488,755,341,489,219,671,642,875
884,60,949,97,626,597,472,371,273,464,942,254,497,443,50,555,692,286,557,445
159,512,555,651,88,237,71,259,76,639,727,356,519,93,696,644,872,117,160,655
897,767,193,255,485,702,370,160,597,651,918,444,831,160,67,107,768,140,163,282
523,415,900,125,409,75,335,512,807,507,769,73,108,427,269,826,817,434,946,80
114,60,239,55,73,122,619,799,754,795,497,792,835,311,594,767,821,267,812,597
795,291,757,746,626,752,220,649,269,918,75,895,895,369,310,794,638,900,712,619
740,295,117,790,364,344,900,921,884,896,809,382,189,944,165,92,878,791,827,212
256,293,876,370,159,678,669,512,755,185,430,489,515,457,467,312,384,219,380,830
186,130,560,633,920,457,59,766,305,835,642,813,68,453,656,429,427,256,364,296
281,488,117,820,159,444,923,325,805,801,91,698,631,343,131,287,560,831,495,661
132,875,622,812,308,880,160,830,668,238,445,454,410,685,64,413,428,799,55,656
261,772,752,829,367,947,71,194,66,254,102,812,280,455,90,744,823,460,205,406
656,347,472,489,419,355,693,250,221,75,302,492,83,617,691,556,687,99,773,520
208,365,163,0,181,820,403,844,343,347,557,124,945,599,699,439,75,800,745,115
278,228,294,803,372,759,239,384,80,243,99,456,378,367,668,703,762,288,758,689
89,198,186,409,123,279,100,367,275,399,470,163,752,215,659,342,69,916,467,875
624,551,663,437,441,753,807,638,373,881,108,377,229,367,769,691,79,254,409,456
661,553,822,674,435,55,800,139,749,800,158,368,402,521,321,842,285,439,673,417
218,363,786,191,694,117,130,95,701,284,159,308,802,400,826,284,158,462,405,234
887,763,452,724,336,882,818,377,400,681,674,814,511,470,260,433,97,653,62,744
690,606,756,361,283,670,501,621,519,325,764,239,137,501,62,454,241,237,368,507
61,283,521,131,751,521,696,181,214,766,762,503,190,336,311,345,74,600,617,789
297,375,215,56,675,695,825,125,277,84,656,181,563,790,828,694,343,710,744,298
412,359,842,243,520,876,696,555,620,190,668,487,274,238,599,54,633,297,727,637
690,556,264,384,369,18,190,808,344,603,767,90,695,219,63,896,484,255,483,799
122,877,512,905,254,495,692,751,369,675,625,640,355,879,604,627,457,70,878,78
942,121,807,564,919,431,768,675,65,619,461,336,247,623,527,493,133,283,237,404
84,384,876,444,880,403,675,114,632,255,21,205,339,253,62,372,404,683,292,88
185,348,472,400,63,444,80,883,373,336,426,563,675,561,305,516,449,456,514,872
648,82,604,650,697,825,462,813,306,94,814,597,879,795,461,294,213,511,331,487
488,761,215,264,421,492,695,191,205,753,918,639,162,317,769,212,123,202,591,795
842,127,163,78,765,180,236,87,235,462,60,800,871,364,217,614,924,597,247,409
807,423,611,589,759,629,192,471,456,118,77,760,94,82,882,429,60,462,499,898
772,503,822,287,342,458,918,633,624,216,280,75,328,125,352,685,520,769,508,655
212,386,347,829,752,482,690,521,136,687,991,899,244,798,562,424,354,554,654,61
558,252,63,674,882,420,693,273,604,269,812,621,266,338,697,479,58,295,659,204
351,426,373,683,869,621,815,263,685,244,804,435,446,461,353,764,762,815,403,760
590,469,920,421,125,382,650,844,694,602,493,746,372,874,243,990,198,486,745,100
249,668,621,369,630,216,242,752,588,10,125,216,675,162,162,352,462,242,296,771
161,81,595,194,61,359,300,379,339,696,58,485,282,696,11,265,302,621,678,439
256,944,238,602,599,184,410,229,244,899,509,289,119,488,159,75,79,269,607,809
992,802,308,271,58,520,201,64,164,748,551,123,371,122,602,403,361,205,820,443
662,601,606,596,57,757,160,687,139,215,783,72,444,440,365,298,511,654,56,237
460,302,355,632,824,664,760,210,924,673,692,688,763,358,488,419,709,275,663,206
595,420,202,434,454,550,274,745,453,195,314,374,682,372,695,249,65,245,57,680
247,877,682,187,743,288,884,509,281,341,355,499,296,178,310,289,651,659,231,250
601,421,558,658,641,884,104,483,865,647,255,945,439,286,821,697,693,820,700,115
608,944,870,617,414,271,440,404,378,426,714,295,791,89,792,280,654,243,193,273
639,183,837,439,161,696,494,653,86,215,58,550,67,758,355,435,507,214,251,403
757,216,644,124,775,382,159,84,599,381,202,946,672,744,443,426,219,490,246,360
406,214,643,589,107,521,819,124,425,774,339,74,608,654,399,444,624,623,943,250
696,291,829,514,696,472,235,751,602,823,259,416,160,24,250,439,743,164,949,762
807,652,337,772,876,685,899,190,459,358,429,831,125,206,834,655,53,422,453,208
837,881,335,774,884,690,588,441,302,864,53,607,81,140,897,470,258,693,355,507
450,471,55,235,307,383,623,488,662,208,302,844,344,622,137,492,604,633,685,745
244,140,457,495,381,558,264,509,69,703,337,756,774,593,824,361,627,513,899,110
588,675,747,751,348,687,310,212,88,711,433,665,947,247,493,941,182,564,242,803
131,809,52,243,229,244,265,212,282,248,441,246,210,701,506,348,812,52,354,791
195,800,417,404,746,683,488,558,53,625,520,774,201,377,143,73,417,457,556,820
879,365,346,239,821,924,843,844,662,648,828,251,374,78,17,768,453,108,245,265
217,286,600,281,408,676,265,5,311,433,236,134,67,463,380,684,123,292,420,690
753,453,500,898,487,556,185,839,361,521,282,674,617,399,946,100,647,941,874,297
509,403,121,483,371,672,768,181,894,109,486,765,308,55,94,196,400,947,551,665
284,628,619,764,673,117,140,649,275,279,347,696,949,668,479,234,186,125,807,658
159,179,808,697,270,948,744,702,588,878,178,600,466,502,189,513,313,219,844,813
794,89,798,897,762,943,632,181,753,637,113,358,236,882,280,680,67,466,299,873
687,211,824,97,459,945,159,521,517,201,252,355,359,303,635,429,643,135,824,738
366,522,355,949,490,500,425,119,517,212,75,301,636,658,188,635,660,115,838,308
67,693,297,257,461,604,287,92,75,601,773,240,193,292,881,916,694,128,603,594
684,486,773,235,386,773,896,401,894,766,551,632,87,196,462,763,103,417,299,867
601,369,703,467,497,74,420,516,235,450,197,198,820,806,370,942,161,813,943,303
565,669,213,604,349,499,203,553,549,690,590,379,89,649,513,517,420,345,366,317
250,514,752,810,520,254,276,692,90,865,458,657,694,4,117,89,519,158,643,248
809,868,194,665,315,99,504,826,211,335,410,512,701,131,879,797,593,204,509,419
89,666,249,808,190,195,991,186,812,353,188,774,65,700,700,457,498,273,745,879
192,299,357,829,601,455,263,123,245,807,594,139,130,98,103,453,645,400,163,919
757,291,511,756,659,640,878,749,408,452,621,598,128,262,365,805,726,252,159,639
998,361,517,654,745,73,799,64,261,243,618,265,806,416,945,84,686,430,452,702
193,686,757,225,206,358,509,552,522,606,592,748,372,375,507,871,501,99,693,373
800,433,423,244,75,399,822,357,866,613,489,598,405,218,772,100,421,374,812,428
232,658,918,309,335,250,271,237,756,115,514,74,254,220,242,130,120,260,691,429
516,135,63,608,68,366,260,827,599,687,433,381,192,464,75,640,890,132,590,592
293,790,666,369,497,824,195,882,100,63,894,386,872,703,511,679,684,639,82,477
112,54,444,68,946,797,370,343,685,588,759,791,499,249,241,941,374,434,239,443
347,666,104,948,623,826,680,277,341,57,411,624,443,455,51,548,290,668,693,502
465,270,252,463,253,434,128,595,774,256,598,64,67,307,348,213,478,348,809,262
278,381,798,768,516,825,831,426,114,181,74,274,772,187,750,799,374,161,3,60
489,340,296,553,96,805,239,648,791,309,484,88,484,797,363,829,128,120,868,977
275,902,677,688,488,867,751,98,874,443,236,379,203,486,200,895,431,241,251,617
187,511,602,442,301,631,876,793,510,623,75,56,101,407,805,164,772,302,608,910
341,194,268,818,450,467,82,262,260,874,185,92,943,436,164,287,644,672,190,949
521,644,922,869,471,467,134,209,878,249,805,259,640,140,820,868,680,867,797,888
696,92,208,819,197,486,240,70,114,697,768,922,52,182,227,414,659,216,745,921
360,764,235,823,822,195,498,290,677,989,811,666,876,872,666,418,484,310,268,206
806,773,119,191,642,746,417,125,946,770,68,386,639,484,847,819,91,452,264,67
894,420,617,399,594,921,811,679,869,642,403,350,816,671,703,279,612,745,271,766
452,724,361,759,428,754,626,410,190,210,217,306,879,51,829,936,603,165,80,279
135,93,678,283,624,488,326,755,240,384,56,641,502,50,790,99,756,816,57,899
468,89,447,490,129,650,796,802,617,403,75,598,827,470,136,826,924,599,510,69
11,519,284,210,795,452,503,701,666,878,300,865,689,632,132,456,269,341,640,289
274,299,214,499,693,677,430,499,427,280,415,554,304,126,509,740,724,823,287,498
702,401,94,647,999,340,100,682,210,412,348,762,625,864,64,661,403,97,697,384
697,695,226,292,556,658,771,802,515,309,797,588,652,509,379,508,115,365,285,452
184,672,373,894,697,699,489,630,269,455,749,352,208,412,512,648,231,295,517,648
116,341,746,199,120,372,89,782,656,620,417,199,379,820,94,668,873,385,818,482
71,437,428,588,87,129,797,604,308,942,148,127,455,252,180,335,343,373,121,774
743,193,820,873,595,357,819,305,409,747,228,763,872,506,84,562,180,809,670,661
943,442,899,309,767,137,199,407,679,944,304,357,792,979,190,198,278,419,214,798
460,413,257,872,134,666,943,446,644,160,549,359,129,684,344,341,633,335,517,662
122,277,89,487,684,358,550,722,97,643,72,361,495,370,919,124,651,651,900,697
817,802,682,797,412,649,506,495,644,897,51,821,471,683,696,384,160,52,112,828
899,483,853,804,384,607,82,91,656,815,624,687,554,820,125,188,78,289,183,656
713,408,672,270,350,123,159,879,746,654,53,506,249,804,259,132,374,128,384,84
51,746,949,761,697,518,884,649,426,99,124,924,631,255,293,633,701,798,21,376
483,294,192,212,455,359,337,814,949,495,164,766,281,799,729,211,515,96,257,754
820,368,756,16,657,651,797,422,601,674,187,234,443,765,883,52,644,262,399,277
374,182,140,695,504,620,617,675,363,52,615,380,878,268,441,756,672,72,352,195
302,201,406,506,483,499,198,120,689,560,411,57,506,622,931,698,188,865,282,597
149,813,402,366,896,264,499,99,68,502,804,923,798,866,882,161,646,193,666,688
773,827,126,773,948,553,808,482,336,990,165,384,821,831,870,62,750,118,814,55
402,669,320,258,631,271,876,201,129,311,373,98,486,666,596,806,949,114,638,252
511,878,125,191,340,868,349,813,100,444,517,303,746,288,670,623,59,664,86,835
58,652,898,548,501,122,644,561,591,379,660,513,751,367,893,750,826,560,867,826
760,799,874,623,304,759,880,946,211,947,180,617,671,215,654,343,161,383,267,148
554,649,296,248,807,69,335,703,371,943,139,456,944,763,772,845,465,549,638,106
382,339,199,347,351,96,864,165,125,65,464,650,820,87,827,199,110,287,922,307
854,408,123,371,134,798,756,278,923,283,492,864,385,563,565,190,252,486,482,630
383,592,2,484,65,922,644,345,793,386,423,679,348,817,471,281,880,415,179,623
306,452,549,877,132,81,454,553,179,343,94,502,72,204,139,678,289,9,413,804
629,424,490,307,695,433,64,95,949,693,378,191,296,72,198,434,485,445,256,89
755,809,606,499,74,259,94,649,315,667,297,88,254,425,241,52,255,352,685,657
768,828,654,691,254,461,241,108,63,661,817,617,17,602,771,753,180,307,635,441
490,699,275,651,456,681,432,335,552,377,279,124,594,869,53,872,788,98,63,769
297,625,382,211,694,408,897,510,196,195,455,339,351,807,760,802,910,71,649,828
483,555,88,691,442,868,289,643,74,403,260,633,561,437,665,460,419,277,154,549
520,411,599,807,278,486,555,165,900,218,500,752,828,250,68,791,200,103,124,188
506,841,843,244,375,303,158,487,134,759,235,763,558,597,805,257,469,274,877,50
628,192,375,975,517,138,180,677,305,60,276,134,817,691,551,214,284,794,51,67
352,642,494,845,634,746,71,619,402,227,808,360,819,920,617,753,643,491,812,492
381,296,293,139,455,643,140,294,245,505,921,201,378,443,800,369,976,879,92,267
918,268,63,181,372,78,264,63,638,236,837,266,644,399,702,257,946,824,869,138
509,206,617,373,55,321,662,376,664,692,458,218,211,560,399,459,163,421,289,483
104,724,435,627,120,348,123,272,304,199,423,190,865,749,234,204,942,894,770,493
180,764,752,135,212,630,554,427,607,621,811,212,362,347,239,777,634,900,455,877
644,946,151,844,220,288,608,385,159,278,370,491,362,949,680,281,871,179,75,386
878,820,458,92,289,195,66,814,362,137,461,127,770,412,916,453,98,797,668,370
385,770,241,744,555,809,268,443,119,132,470,377,74,184,253,122,141,746,197,201
384,667,617,103,869,871,799,257,792,488,127,384,269,680,551,505,280,431,269,254
482,702,159,489,830,123,215,204,872,56,514,260,456,108,368,229,242,191,53,799
602,558,864,268,802,434,160,644,102,592,945,411,607,360,493,796,468,384,386,404
164,371,220,434,628,418,82,588,190,560,608,131,916,694,884,198,765,703,358,82
491,490,263,825,565,509,53,670,416,703,877,126,161,944,76,486,747,784,288,266
679,419,626,341,588,364,758,594,671,51,913,795,261,827,651,633,386,115,626,648
264,621,203,521,366,96,881,431,818,557,356,590,236,383,344,941,655,628,382,227
901,499,378,762,488,671,350,255,876,239,406,556,683,521,158,421,829,373,158,72
624,900,869,467,444,820,247,280,291,234,896,747,899,654,184,471,622,13,871,471
799,683,279,131,663,678,225,676,430,65,345,98,138,193,188,267,505,257,689,588
766,305,865,416,60,516,771,462,165,105,483,555,883,761,498,665,660,696,617,506
469,431,658,439,267,163,505,194,698,681,494,258,408,107,669,294,809,136,549,288
417,440,178,259,816,193,502,90,945,991,307,465,343,564,488,118,139,798,441,824
946,683,592,182,813,74,864,872,408,640,460,948,77,263,692,467,402,202,11,108
607,214,949,219,466,431,486,280,635,342,254,405,793,374,256,94,692,552,615,261
497,681,195,924,877,92,198,186,308,403,250,372,484,301,111,187,56,201,401,193
549,608,490,811,549,284,335,648,2,684,920,165,277,866,749,400,604,278,461,202
122,826,658,844,270,817,896,340,656,784,876,340,306,383,589,647,797,296,220,605
671,804,653,297,61,340,239,772,373,688,291,755,92,240,371,65,21,604,607,642
994,381,193,868,76,495,943,403,415,84,423,626,99,675,214,344,805,588,115,410
646,276,478,845,116,947,564,462,407,689,91,284,257,59,64,596,287,292,214,286
250,668,109,239,701,646,347,278,440,210,108,185,670,238,556,884,180,415,405,310
56,159,267,821,744,435,762,658,657,262,827,196,870,352,713,873,682,73,71,724
677,494,594,700,597,551,767,138,749,430,124,560,339,386,278,200,896,94,139,712
938,73,489,383,346,635,638,747,821,345,408,758,800,431,765,183,842,263,186,745
5,125,769,508,404,250,747,818,458,757,54,875,651,803,896,250,797,589,293,636
642,342,361,132,598,83,629,443,336,213,77,829,208,295,811,379,269,192,449,235
303,794,376,117,198,874,88,284,241,565,632,425,240,57,768,398,606,685,516,212
291,819,947,878,829,423,410,880,7,101,379,761,595,867,384,559,64,896,92,664
263,654,441,635,564,661,914,640,668,268,290,344,286,757,490,588,818,765,421,305
655,622,797,562,414,85,179,375,867,801,418,460,69,276,158,109,140,302,212,381
466,217,763,790,486,202,57,124,878,122,239,520,774,628,502,749,357,604,862,92
479,549,68,134,238,687,796,368,817,209,252,301,495,918,682,161,409,247,897,81
254,451,894,681,618,437,509,791,592,454,349,258,456,282,793,254,793,56,820,158
800,185,138,434,291,19,134,140,759,765,288,178,268,621,218,439,291,502,496,52
373,810,255,509,189,84,756,746,498,364,216,824,774,656,392,765,370,199,771,304
650,443,845,605,900,340,189,124,259,820,608,810,761,370,242,555,834,800,752,507
441,757,425,831,636,139,448,746,98,249,895,184,454,442,756,685,432,553,120,634
115,563,74,562,841,823,501,945,671,354,680,279,604,772,279,194,286,257,258,272
414,455,515,162,53,505,165,554,441,422,369,367,297,220,755,516,849,554,191,132
620,139,813,95,354,241,493,880,652,901,408,98,431,866,695,66,119,664,80,202
589,373,596,461,340,335,286,695,766,423,695,626,470,550,882,367,897,838,382,943
374,339,518,555,212,409,511,109,687,592,338,77,831,588,897,164,163,508,603,416
634,767,376,844,749,803,383,53,752,274,96,116,628,549,126,450,465,179,865,554
115,821,821,383,605,275,619,654,564,819,799,644,651,431,430,114,804,165,907,482
649,452,253,493,680,366,761,677,794,501,207,806,822,92,683,811,618,229,881,435
421,489,178,459,402,436,216,103,272,498,675,341,811,369,875,758,418,702,246,344
429,805,100,604,420,436,465,304,342,818,126,517,65,552,899,858,67,270,634,483
186,98,22,429,795,453,774,58,924,431,753,266,827,65,627,667,797,140,805,116
645,692,67,515,189,455,820,195,872,54,750,63,442,806,614,71,818,134,697,265
644,209,487,486,751,68,243,494,744,810,351,431,72,621,61,584,266,411,470,99
824,790,625,384,96,629,195,749,440,557,633,83,211,983,354,655,178,195,646,73
309,342,684,275,288,621,430,347,135,84,549,203,631,428,755,472,588,386,786,472
805,455,309,139,845,992,702,353,621,307,123,68,694,404,516,755,699,122,620,192
814,880,192,466,68,645,119,509,337,671,238,813,134,894,896,298,469,263,254,858
197,634,618,115,559,180,632,831,772,497,234,342,92,517,130,562,935,499,347,899
253,104,423,752,278,341,339,108,459,193,829,671,670,603,752,374,751,497,430,793
273,80,79,101,69,442,381,472,117,118,747,76,633,108,446,634,554,291,306,400
86,245,132,135,101,420,262,664,442,765,551,703,820,293,703,890,460,899,434,264
789,748,257,799,680,696,350,604,92,362,679,260,336,842,468,924,490,262,191,131
208,941,258,823,87,11,746,419,364,492,440,66,405,245,211,182,376,257,287,829
842,807,739,773,633,411,471,595,659,50,464,276,867,266,122,767,290,866,494,406
519,696,438,924,430,287,444,265,245,608,415,120,77,642,878,99,60,309,104,125
81,62,295,220,284,286,590,414,651,16,240,873,279,629,270,78,698,560,754,796
501,378,589,256,724,206,698,873,383,404,443,628,633,245,652,838,829,628,651,192
101,943,695,519,359,865,132,246,206,767,871,922,85,288,645,533,629,462,133,601
755,632,54,459,801,69,24,63,367,81,770,680,235,688,414,210,747,409,761,632
18,434,493,136,114,368,452,503,379,687,671,80,640,422,256,641,299,560,666,135
129,347,747,259,435,436,64,100,403,416,453,415,92,468,194,120,486,111,218,628
374,381,708,99,404,372,502,99,648,945,624,919,461,792,81,469,116,744,60,690
208,131,218,115,658,695,756,184,599,159,820,138,472,667,779,137,276,680,196,506
594,761,703,487,67,218,84,67,790,470,130,750,383,687,380,900,199,610,242,594
364,501,597,753,130,619,220,69,520,404,945,415,556,439,552,716,811,756,62,459
595,179,510,773,606,647,518,55,998,256,830,617,413,433,688,127,139,805,186,845
243,472,648,340,911,201,415,460,432,516,793,416,884,799,800,83,949,62,758,50
118,89,942,439,340,278,137,908,135,699,453,383,287,194,403,501,829,242,54,879
462,461,655,114,504,463,256,362,340,414,463,416,769,808,864,127,565,373,662,615
266,706,116,219,246,69,620,75,600,50,553,831,440,342,919,99,271,76,680,215
899,344,676,979,372,270,274,201,84,161,409,593,250,194,514,206,380,309,352,399"""

ticket = [[str(i) for i in ticket]]
rules = rules.split("\n")
allTickets = [n.split(",") for n in other_ticket.split("\n")]
print("---------------------------- Part 1\r\n")
sol = Solution()
res, invalidTickets = sol.countInvalidTickets(rules, ticket, allTickets)
print(res)

print("---------------------------- Part 2\r\n")
newTickets = []
for i, old_ticket in enumerate(allTickets):
    if i not in invalidTickets:
        newTickets.append(old_ticket)

newTickets = ticket + newTickets
res = sol.matchFields(rules, newTickets)
print(res)