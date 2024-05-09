import time
from binary_search import *

lista = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70, 73, 76, 79, 82, 85, 88, 91, 94, 97, 100, 103, 106, 109, 112, 115, 118, 121, 124, 127, 130, 133, 136, 139, 142, 145, 148, 151, 154, 157, 160, 163, 166, 169, 172, 175, 178, 181, 184, 187, 190, 193, 196, 199, 202, 205, 208, 211, 214, 217, 220, 223, 226, 229, 232, 235, 238, 241, 244, 247, 250, 253, 256, 259, 262, 265, 268, 271, 274, 277, 280, 283, 286, 289, 292, 295, 298, 301, 304, 307, 310, 313, 316, 319, 322, 325, 328, 331, 334, 337, 340, 343, 346, 349, 352, 355, 358, 361, 364, 367, 370, 373, 376, 379, 382, 385, 388, 391, 394, 397, 400, 403, 406, 409, 412, 415, 418, 421, 424, 427, 430, 433, 436, 439, 442, 445, 448, 451, 454, 457, 460, 463, 466, 469, 472, 475, 478, 481, 484, 487, 490, 493, 496, 499, 502, 505, 508, 511, 514, 517, 520, 523, 526, 529, 532, 535, 538, 541, 544, 547, 550, 553, 556, 559, 562, 565, 568, 571, 574, 577, 580, 583, 586, 589, 592, 595, 598, 601, 604, 607, 610, 613, 616, 619, 622, 625, 628, 631, 634, 637, 640, 643, 646, 649, 652, 655, 658, 661, 664, 667, 670, 673, 676, 679, 682, 685, 688, 691, 694, 697, 700, 703, 706, 709, 712, 715, 718, 721, 724, 727, 730, 733, 736, 739, 742, 745, 748, 751, 754, 757, 760, 763, 766, 769, 772, 775, 778, 781, 784, 787, 790, 793, 796, 799, 802, 805, 808, 811, 814, 817, 820, 823, 826, 829, 832, 835, 838, 841, 844, 847, 850, 853, 856, 859, 862, 865, 868, 871, 874, 877, 880, 883, 886, 889, 892, 895, 898, 901, 904, 907, 910, 913, 916, 919, 922, 925, 928, 931, 934, 937, 940, 943, 946, 949, 952, 955, 958, 961, 964, 967, 970, 973, 976, 979, 982, 985, 988, 991, 994, 997, 1000, 1003, 1006, 1009, 1012, 1015, 1018, 1021, 1024, 1027, 1030, 1033, 1036, 1039, 1042, 1045, 1048, 1051, 1054, 1057, 1060, 1063, 1066, 1069, 1072, 1075, 1078, 1081, 1084, 1087, 1090, 1093, 1096, 1099, 1102, 1105, 1108, 1111, 1114, 1117, 1120, 1123, 1126, 1129, 1132, 1135, 1138, 1141, 1144, 1147, 1150, 1153, 1156, 1159, 1162, 1165, 1168, 1171, 1174, 1177, 1180, 1183, 1186, 1189, 1192, 1195, 1198, 1201, 1204, 1207, 1210, 1213, 1216, 1219, 1222, 1225, 1228, 1231, 1234, 1237, 1240, 1243, 1246, 1249, 1252, 1255, 1258, 1261, 1264, 1267, 1270, 1273, 1276, 1279, 1282, 1285, 1288, 1291, 1294, 1297, 1300, 1303, 1306, 1309, 1312, 1315, 1318, 1321, 1324, 1327, 1330, 1333, 1336, 1339, 1342, 1345, 1348, 1351, 1354, 1357, 1360, 1363, 1366, 1369, 1372, 1375, 1378, 1381, 1384, 1387, 1390, 1393, 1396, 1399, 1402, 1405, 1408, 1411, 1414, 1417, 1420, 1423, 1426, 1429, 1432, 1435, 1438, 1441, 1444, 1447, 1450, 1453, 1456, 1459, 1462, 1465, 1468, 1471, 1474, 1477, 1480, 1483, 1486, 1489, 1492, 1495, 1498, 1501, 1504, 1507, 1510, 1513, 1516, 1519, 1522, 1525, 1528, 1531, 1534, 1537, 1540, 1543, 1546, 1549, 1552, 1555, 1558, 1561, 1564, 1567, 1570, 1573, 1576, 1579, 1582, 1585, 1588, 1591, 1594, 1597, 1600, 1603, 1606, 1609, 1612, 1615, 1618, 1621, 1624, 1627, 1630, 1633, 1636, 1639, 1642, 1645, 1648, 1651, 1654, 1657, 1660, 1663, 1666, 1669, 1672, 1675, 1678, 1681, 1684, 1687, 1690, 1693, 1696, 1699, 1702, 1705, 1708, 1711, 1714, 1717, 1720, 1723, 1726, 1729, 1732, 1735, 1738, 1741, 1744, 1747, 1750, 1753, 1756, 1759, 1762, 1765, 1768, 1771, 1774, 1777, 1780, 1783, 1786, 1789, 1792, 1795, 1798, 1801, 1804, 1807, 1810, 1813, 1816, 1819, 1822, 1825, 1828, 1831, 1834, 1837, 1840, 1843, 1846, 1849, 1852, 1855, 1858, 1861, 1864, 1867, 1870, 1873, 1876, 1879, 1882, 1885, 1888, 1891, 1894, 1897, 1900, 1903, 1906, 1909, 1912, 1915, 1918, 1921, 1924, 1927, 1930, 1933, 1936, 1939, 1942, 1945, 1948, 1951, 1954, 1957, 1960, 1963, 1966, 1969, 1972, 1975, 1978, 1981, 1984, 1987, 1990, 1993, 1996, 1999, 2002, 2005, 2008, 2011, 2014, 2017, 2020, 2023, 2026, 2029, 2032, 2035, 2038, 2041, 2044, 2047, 2050, 2053, 2056, 2059, 2062, 2065, 2068, 2071, 2074, 2077, 2080, 2083, 2086, 2089, 2092, 2095, 2098, 2101, 2104, 2107, 2110, 2113, 2116, 2119, 2122, 2125, 2128, 2131, 2134, 2137, 2140, 2143, 2146, 2149, 2152, 2155, 2158, 2161, 2164, 2167, 2170, 2173, 2176, 2179, 2182, 2185, 2188, 2191, 2194, 2197, 2200, 2203, 2206, 2209, 2212, 2215, 2218, 2221, 2224, 2227, 2230, 2233, 2236, 2239, 2242, 2245, 2248, 2251, 2254, 2257, 2260, 2263, 2266, 2269, 2272, 2275, 2278, 2281, 2284, 2287, 2290, 2293, 2296, 2299, 2302, 2305, 2308, 2311, 2314, 2317, 2320, 2323, 2326, 2329, 2332, 2335, 2338, 2341, 2344, 2347, 2350, 2353, 2356, 2359, 2362, 2365, 2368, 2371, 2374, 2377, 2380, 2383, 2386, 2389, 2392, 2395, 2398, 2401, 2404, 2407, 2410, 2413, 2416, 2419, 2422, 2425, 2428, 2431, 2434, 2437, 2440, 2443, 2446, 2449, 2452, 2455, 2458, 2461, 2464, 2467, 2470, 2473, 2476, 2479, 2482, 2485, 2488, 2491, 2494, 2497, 2500, 2503, 2506, 2509, 2512, 2515, 2518, 2521, 2524, 2527, 2530, 2533, 2536, 2539, 2542, 2545, 2548, 2551, 2554, 2557, 2560, 2563, 2566, 2569, 2572, 2575, 2578, 2581, 2584, 2587, 2590, 2593, 2596, 2599, 2602, 2605, 2608, 2611, 2614, 2617, 2620, 2623, 2626, 2629, 2632, 2635, 2638, 2641, 2644, 2647, 2650, 2653, 2656, 2659, 2662, 2665, 2668, 2671, 2674, 2677, 2680, 2683, 2686, 2689, 2692, 2695, 2698, 2701, 2704, 2707, 2710, 2713, 2716, 2719, 2722, 2725, 2728, 2731, 2734, 2737, 2740, 2743, 2746, 2749, 2752, 2755, 2758, 2761, 2764, 2767, 2770, 2773, 2776, 2779, 2782, 2785, 2788, 2791, 2794, 2797, 2800, 2803, 2806, 2809, 2812, 2815, 2818, 2821, 2824, 2827, 2830, 2833, 2836, 2839, 2842, 2845, 2848, 2851, 2854, 2857, 2860, 2863, 2866, 2869, 2872, 2875, 2878, 2881, 2884, 2887, 2890, 2893, 2896, 2899, 2902, 2905, 2908, 2911, 2914, 2917, 2920, 2923, 2926, 2929, 2932, 2935, 2938, 2941, 2944, 2947, 2950, 2953, 2956, 2959, 2962, 2965, 2968, 2971, 2974, 2977, 2980, 2983, 2986, 2989, 2992, 2995, 2998, 3001, 3004, 3007, 3010, 3013, 3016, 3019, 3022, 3025, 3028, 3031, 3034, 3037, 3040, 3043, 3046, 3049, 3052, 3055, 3058, 3061, 3064, 3067, 3070, 3073, 3076, 3079, 3082, 3085, 3088, 3091, 3094, 3097, 3100, 3103, 3106, 3109, 3112, 3115, 3118, 3121, 3124, 3127, 3130, 3133, 3136, 3139, 3142, 3145, 3148, 3151, 3154, 3157, 3160, 3163, 3166, 3169, 3172, 3175, 3178, 3181, 3184, 3187, 3190, 3193, 3196, 3199, 3202, 3205, 3208, 3211, 3214, 3217, 3220, 3223, 3226, 3229, 3232, 3235, 3238, 3241, 3244, 3247, 3250, 3253, 3256, 3259, 3262, 3265, 3268, 3271, 3274, 3277, 3280, 3283, 3286, 3289, 3292, 3295, 3298, 3301, 3304, 3307, 3310, 3313, 3316, 3319, 3322, 3325, 3328, 3331, 3334, 3337, 3340, 3343, 3346, 3349, 3352, 3355, 3358, 3361, 3364, 3367, 3370, 3373, 3376, 3379, 3382, 3385, 3388, 3391, 3394, 3397, 3400, 3403, 3406, 3409, 3412, 3415, 3418, 3421, 3424, 3427, 3430, 3433, 3436, 3439, 3442, 3445, 3448, 3451, 3454, 3457, 3460, 3463, 3466, 3469, 3472, 3475, 3478, 3481, 3484, 3487, 3490, 3493, 3496, 3499, 3502, 3505, 3508, 3511, 3514, 3517, 3520, 3523, 3526, 3529, 3532, 3535, 3538, 3541, 3544, 3547, 3550, 3553, 3556, 3559, 3562, 3565, 3568, 3571, 3574, 3577, 3580, 3583, 3586, 3589, 3592, 3595, 3598, 3601, 3604, 3607, 3610, 3613, 3616, 3619, 3622, 3625, 3628, 3631, 3634, 3637, 3640, 3643, 3646, 3649, 3652, 3655, 3658, 3661, 3664, 3667, 3670, 3673, 3676, 3679, 3682, 3685, 3688, 3691, 3694, 3697, 3700, 3703, 3706, 3709, 3712, 3715, 3718, 3721, 3724, 3727, 3730, 3733, 3736, 3739, 3742, 3745, 3748, 3751, 3754, 3757, 3760, 3763, 3766, 3769, 3772, 3775, 3778, 3781, 3784, 3787, 3790, 3793, 3796, 3799, 3802, 3805, 3808, 3811, 3814, 3817, 3820, 3823, 3826, 3829, 3832, 3835, 3838, 3841, 3844, 3847, 3850, 3853, 3856, 3859, 3862, 3865, 3868, 3871, 3874, 3877, 3880, 3883, 3886, 3889, 3892, 3895, 3898, 3901, 3904, 3907, 3910, 3913, 3916, 3919, 3922, 3925, 3928, 3931, 3934, 3937, 3940, 3943, 3946, 3949, 3952, 3955, 3958, 3961, 3964, 3967, 3970, 3973, 3976, 3979, 3982, 3985, 3988, 3991, 3994, 3997, 4000, 4003, 4006, 4009, 4012, 4015, 4018, 4021, 4024, 4027, 4030, 4033, 4036, 4039, 4042, 4045, 4048, 4051, 4054, 4057, 4060, 4063, 4066, 4069, 4072, 4075, 4078, 4081, 4084, 4087, 4090, 4093, 4096, 4099, 4102, 4105, 4108, 4111, 4114, 4117, 4120, 4123, 4126, 4129, 4132, 4135, 4138, 4141, 4144, 4147, 4150, 4153, 4156, 4159, 4162, 4165, 4168, 4171, 4174, 4177, 4180, 4183, 4186, 4189, 4192, 4195, 4198, 4201, 4204, 4207, 4210, 4213, 4216, 4219, 4222, 4225, 4228, 4231, 4234, 4237, 4240, 4243, 4246, 4249, 4252, 4255, 4258, 4261, 4264, 4267, 4270, 4273, 4276, 4279, 4282, 4285, 4288, 4291, 4294, 4297, 4300, 4303, 4306, 4309, 4312, 4315, 4318, 4321, 4324, 4327, 4330, 4333, 4336, 4339, 4342, 4345, 4348, 4351, 4354, 4357, 4360, 4363, 4366, 4369, 4372, 4375, 4378, 4381, 4384, 4387, 4390, 4393, 4396, 4399, 4402, 4405, 4408, 4411, 4414, 4417, 4420, 4423, 4426, 4429, 4432, 4435, 4438, 4441, 4444, 4447, 4450, 4453, 4456, 4459, 4462, 4465, 4468, 4471, 4474, 4477, 4480, 4483, 4486, 4489, 4492, 4495, 4498, 4501, 4504, 4507, 4510, 4513, 4516, 4519, 4522, 4525, 4528, 4531, 4534, 4537, 4540, 4543, 4546, 4549, 4552, 4555, 4558, 4561, 4564, 4567, 4570, 4573, 4576, 4579, 4582, 4585, 4588, 4591, 4594, 4597, 4600, 4603, 4606, 4609, 4612, 4615, 4618, 4621, 4624, 4627, 4630, 4633, 4636, 4639, 4642, 4645, 4648, 4651, 4654, 4657, 4660, 4663, 4666, 4669, 4672, 4675, 4678, 4681, 4684, 4687, 4690, 4693, 4696, 4699, 4702, 4705, 4708, 4711, 4714, 4717, 4720, 4723, 4726, 4729, 4732, 4735, 4738, 4741, 4744, 4747, 4750, 4753, 4756, 4759, 4762, 4765, 4768, 4771, 4774, 4777, 4780, 4783, 4786, 4789, 4792, 4795, 4798, 4801, 4804, 4807, 4810, 4813, 4816, 4819, 4822, 4825, 4828, 4831, 4834, 4837, 4840, 4843, 4846, 4849, 4852, 4855, 4858, 4861, 4864, 4867, 4870, 4873, 4876, 4879, 4882, 4885, 4888, 4891, 4894, 4897, 4900, 4903, 4906, 4909, 4912, 4915, 4918, 4921, 4924, 4927, 4930, 4933, 4936, 4939, 4942, 4945, 4948, 4951, 4954, 4957, 4960, 4963, 4966, 4969, 4972, 4975, 4978, 4981, 4984, 4987, 4990, 4993, 4996, 4999, 5002, 5005, 5008, 5011, 5014, 5017, 5020, 5023, 5026, 5029, 5032, 5035, 5038, 5041, 5044, 5047, 5050, 5053, 5056, 5059, 5062, 5065, 5068, 5071, 5074, 5077, 5080, 5083, 5086, 5089, 5092, 5095, 5098, 5101, 5104, 5107, 5110, 5113, 5116, 5119, 5122, 5125, 5128, 5131, 5134, 5137, 5140, 5143, 5146, 5149, 5152, 5155, 5158, 5161, 5164, 5167, 5170, 5173, 5176, 5179, 5182, 5185, 5188, 5191, 5194, 5197, 5200, 5203, 5206, 5209, 5212, 5215, 5218, 5221, 5224, 5227, 5230, 5233, 5236, 5239, 5242, 5245, 5248, 5251, 5254, 5257, 5260, 5263, 5266, 5269, 5272, 5275, 5278, 5281, 5284, 5287, 5290, 5293, 5296, 5299, 5302, 5305, 5308, 5311, 5314, 5317, 5320, 5323, 5326, 5329, 5332, 5335, 5338, 5341, 5344, 5347, 5350, 5353, 5356, 5359, 5362, 5365, 5368, 5371, 5374, 5377, 5380, 5383, 5386, 5389, 5392, 5395, 5398, 5401, 5404, 5407, 5410, 5413, 5416, 5419, 5422, 5425, 5428, 5431, 5434, 5437, 5440, 5443, 5446, 5449, 5452, 5455, 5458, 5461, 5464, 5467, 5470, 5473, 5476, 5479, 5482, 5485, 5488, 5491, 5494, 5497, 5500, 5503, 5506, 5509, 5512, 5515, 5518, 5521, 5524, 5527, 5530, 5533, 5536, 5539, 5542, 5545, 5548, 5551, 5554, 5557, 5560, 5563, 5566, 5569, 5572, 5575, 5578, 5581, 5584, 5587, 5590, 5593, 5596, 5599, 5602, 5605, 5608, 5611, 5614, 5617, 5620, 5623, 5626, 5629, 5632, 5635, 5638, 5641, 5644, 5647, 5650, 5653, 5656, 5659, 5662, 5665, 5668, 5671, 5674, 5677, 5680, 5683, 5686, 5689, 5692, 5695, 5698, 5701, 5704, 5707, 5710, 5713, 5716, 5719, 5722, 5725, 5728, 5731, 5734, 5737, 5740, 5743, 5746, 5749, 5752, 5755, 5758, 5761, 5764, 5767, 5770, 5773, 5776, 5779, 5782, 5785, 5788, 5791]

def search_item(array, value):
    index = None
    for i in range(len(array)-1):
        if array[i] == value:
            index = i
    return index

start = time.time()
x = binary_search(lista,3760,0,len(lista) -1)
print(x)
end = time.time()
print(f"Busqueda binaria: {(end-start)*1000} ms")


start = time.time()
x = search_item(lista,3760)
print(x)
end = time.time()
print(f"Busqueda normal: {(end-start)*1000} ms")

print(f"La lista tiene: {len(lista)} elementos")