'''
This program returns an integer representing the maximum possible sum of the contiguous subarray using Kadane's Algorithm

- Creating a function maxSubArray() which will take one argument as a List A
- Initializing two variables max_so_far and curr_max which will store the first element in the List A
- Traversing the List A from second element till the last and find the maximum sum from the contiguous subarray
- curr_max will store the maximum value between the current element and the curr_max + current element
- max_so_far will store the maximum value between max_so_far and curr_max
- At last returning the maximum possible sum of the contiguous subarray
'''

def maxSubArray(A):
        max_so_far =A[0] 
        curr_max = A[0] 
        for i in range(1,len(A)): 
            curr_max = max(A[i], curr_max + A[i]) 
            max_so_far = max(max_so_far,curr_max) 
        return max_so_far

if __name__ == "__main__":
    A=[ -342, -193, 47, 33, -346, -245, -161, -153, 23, 99, -239, -256, -141, -94, -473, -185, -56, -243, -95, -118, -77, -122, -46, -56, -276, -208, -469, -429, -193, 61, -302, -247, -388, -348, 1, -431, -130, -216, -324, 12, -195, -408, -191, -368, 93, -269, -386, 43, -334, -19, 18, -291, -257, -325, 11, -200, -266, 85, -496, -30, -369, -236, -465, -476, -478, -211, 45, 56, -485, 11, 3, -201, 3, -22, -260, -400, -393, -422, -463, 79, -77, -114, -81, -301, -115, -102, -299, -468, -339, -433, 66, 53, 49, -343, -342, -189, 0, -392, 76, -226, -273, -355, -256, -317, -188, -286, -351, 59, -88, 65, -57, -67, 30, -92, -400, 9, -459, -334, -342, -259, -217, -330, -126, -279, -190, -350, -60, -437, 58, -143, -209, 60, -333, 68, -358, -335, -214, -186, -130, -54, -17, -480, -489, -448, -352, 40, -64, -469, -355, 24, -282, 6, -63, -325, -93, -60, 59, -307, -201, 79, -90, -61, -52, 77, -172, -18, -203, 6, -99, -303, -365, -256, 18, -252, -188, -128, 20, 48, -285, -135, -405, -462, -53, -61, -259, -423, -357, -224, -319, -305, -235, -360, -319, -70, -210, -364, -101, -205, -307, -165, -84, -497, 50, -366, -339, -262, -129, -410, -35, -236, -28, -486, -14, -267, -95, -424, -38, -424, -378, -237, -155, -386, -247, -186, -285, -489, -26, -148, -429, 64, -27, -358, -338, -469, -8, -330, -242, -434, -49, -385, -326, -2, -406, -372, -483, -69, -420, -116, -498, -484, -242, -441, -18, -395, -116, -297, -163, -238, -269, -472, -15, -69, -340, -498, -387, -365, -412, -413, -180, -104, -427, -306, -143, -228, -473, -475, -177, -105, 47, -408, -401, -118, -157, -27, -182, -319, 63, -300, 6, -64, -22, -68, -395, -423, -499, 34, -184, -238, -386, -54, 61, -25, -12, -285, -112, -145, 32, -294, -10, -325, -132, -143, -201, 53, -393, -33, -77, -300, -252, -123, 99, -39, -289, -415, -280, -163, -77, 53, -183, 32, -479, -358, -188, -42, -73, -130, -215, 75, 0, -80, -396, -145, -286, -443, 77, -296, -100, -410, 11, -417, -371, 8, -123, -341, -487, -419, -256, -179, -62, 90, -290, -400, -217, -240, 60, 26, -320, -227, -349, -295, -489, 15, -42, -267, -43, -77, 28, -456, -312, 68, -445, -230, -375, -47, -218, -344, -9, -196, -327, -336, -459, -93, 40, -166, -270, -52, -392, -271, -19, -419, -405, -499, -395, -257, -411, -289, -362, -242, -398, -147, -410, -62, -399, 15, -449, -286, -25, -319, -446, -422, -174, -439, -218, -230, -64, -96, -473, -252, 64, -284, -94, 41, -375, -273, -22, -363, -133, -172, -185, -99, 90, -360, -201, -395, -24, -113, 98, -496, -451, -164, -388, -192, -18, 86, -409, -469, -38, -194, -72, -318, -415, 66, -318, -400, -60, 2, -178, -55, 86, -367, -186, 9, -430, -309, -477, -388, -75, -369, -196, -261, -492, -142, -16, -386, -76, -330, 1, -332, 66, -115, -309, -485, -210, -189, 17, -202, -254, 72, -106, -490, -450, -259, -135, -30, -459, -215, -149, -110, -480, -107, -18, 91, -2, -269, -64, -347, -404, -346, -390, -300, 50, -33, 92, -91, -32, 77, -58, -336, 77, -483, -488, 49, -497, 33, -435, -431, -123, 68, -11, -125, -397, 9, -446, -267, -91, 63, -107, -49, 69, -368, -320, -348, -143, 51, -452, -96, 90, 83, -97, -84, 17, -3, -125, -124, -27, -439, 99, -379, -143, -101, -306, -364, -228, -289, -414, -411, -435, -51, -47, -353, -488, -232, -405, -90, -442, -242, 49, -196, 59, -281, -303, -33, -337, -427, -356, 32, -117, -438, 5, -158, 60, -252, -138, -131, 40, -41, 81, -459, -477, 100, -144, -495, 86, -321, 21, -30, -71, -40, -236, -180, -211, 64, -338, -67, -20, -428, -230, -262, -383, -463, 29, -166, -477, -393, -472, -405, -436, 25, -460, 59, -254, -337, 89, -232, -250, 41, -433, -125, -10, -74, 38, -351, -140, -92, -413, -279, 91, -63, -110, -81, -33, -55, -20, -148, 90, 73, -79, -91, -247, -219, -185, -133, -392, -427, -253, 65, -410, -368, 57, -66, -108, 90, -437, -90, -346, -51, -198, -287, 96, -386, 71, -406, -282, -42, -313, -164, -201, 7, -143, -8, -253, -78, -115, -99, -143, 25, 95, -448, -17, -309, -95, -433, -388, -353, -319, -172, -91, -274, -420, 78, -438, -244, -319, -164, -287, -197, 49, -78, -11, -262, -425, -40, -170, -182, 65, -466, -456, -453, 51, -382, -6, -177, -128, -55, 19, -260, -194, -52, 8, -482, -452, -99, -406, -323, -405, -154, -359, 74, -241, -253, -206, 58, -154, -311, -182, -433, -377, -81, -499, -468, -491, -292, -146, 81, -200, -145, -142, -238, -377, -98, -410, 37, -306, -233, -187, 96, 29, -415, -165, -127, 8, -497, -204, -409, -475, -420, -55, -25, 59, -490, -426, -178, -447, -412, 80, -305, -246, -398, -164, 93, -342, 76, 78, -387, -235, 34, -248, -11, -421, 85, -240, -159, -330, -381, -36, -317, -313, -221, -119, -181, 23, 11, -399, 75, -224, -154, -23, -66, 94, -488, 71, -74, -94, -292, -293, -154, 16, -39, -274, -23, -270, -231, 75, -439, -268, -94, 19, -8, -155, -213, 0, -124, -314, -74, -352, -294, -44, -465, -129, -342, -215, -472, -116, -17, -228, -28, -214, -164, 0, -299, -470, 15, -67, -238, 75, -48, -411, -72, -344, 100, -316, -365, -219, -274, -125, -162, 85, -344, -240, -411, -99, -211, -358, -67, -20, -154, -119, -153, -86, -406, 87, -366, -360, -479, -358, -431, -317, -26, -359, -423, -490, -244, -24, -124, 63, -416, -55, 17, -439, 46, -139, -234, 89, -329, -270, 36, 29, -32, -161, -165, -171, -14, -219, -225, -85, 24, -123, -249, -413, 58, 84, -1, -417, -492, -358, -397, -240, -47, -133, -163, -490, -171, 87, -418, -386, -355, -289, -323, -355, -379, 75, -52, -230, 93, -191, -31, -357, -164, -359, -188 ]
    print(maxSubArray(A))