def flippingMatrix(matrix):
    # Write your code here
    sum = 0
    n = len(matrix)
    m = len(matrix[0])
    cur, right, down, diag, ans=0,0,0,0,0
    for i in range(n//2):
        for j in range(m//2):
            cur = matrix[i][j]
            right = matrix[i][m-j-1]
            down = matrix[n-i-1][j]
            diag = matrix[n-i-1][m-j-1]
            ans = max(cur, right, down, diag)
            sum += ans
        
    
    return sum
# 
# A utility function to calculate area
# of triangle formed by (x1, y1),
# (x2, y2) and (x3, y3)
def area(x1, y1, x2, y2, x3, y3):

	return abs((x1 * (y2 - y3) + x2 * (y3 - y1)	+ x3 * (y1 - y2)) / 2.0)



# A function to check whether point P(x, y)
# lies inside the triangle formed by
# A(x1, y1), B(x2, y2) and C(x3, y3)
def isInside(x1, y1, x2, y2, x3, y3, x, y):

 

	# Calculate area of triangle ABC
    A = area (x1, y1, x2, y2, x3, y3)

	# Calculate area of triangle PBC
    A1 = area (x, y, x2, y2, x3, y3)
	
	# Calculate area of triangle PAC
    A2 = area (x1, y1, x, y, x3, y3)
	
	# Calculate area of triangle PAB
    A3 = area (x1, y1, x2, y2, x, y)
	
	# Check if sum of A1, A2 and A3
	# is same as A
    if(A == A1 + A2 + A3):
        return True
    else:
        return False

# Driver program to test above function
# Let us check whether the point P(10, 15)
# lies inside the triangle formed by
# A(0, 0), B(20, 0) and C(10, 30)
# if (isInside(0, 0, 2, 0, 0, 3, 3, 1)):
# 	print('Inside')
# else:
# 	print('Not Inside')

if (isInside(0, 0, 2, 0, 0, 3, 0, 0)):
	print('Inside')
else:
	print('Not Inside')    

# This code is contributed by Danish Raza



n="7404954009694227446246375747227852213692570890717884174001587537145838723390362624487926131161112710589127423098959327020544003395792482625191721603328307774998124389641069884634086849138515079220750462317357487762780480576640689175346956135668451835480490089962406773267569650663927778867764315211280625033388271518264961090111547480467065229843613873499846390257375933040086863430523668050046930387013897062106309406874425001127890574986610018093859693455518413268914361859000614904461902442822577552997680098389183082654625098817411306985010658756762152160904278169491634807464356130877526392725432086439934006728914411061861235300979536190100734360684054557448454640750198466877185875290011114667186730452681943043971812380628117527172389889545776779555664826488520325234792648448625225364535053605515386730925070072896004645416713682004600636574389040662827182696337187610904694029221880801372864040345567230941110986028568372710970460116491983700312243090679537497139499778923997433720159174153"
k="100000"

def superDigit(n, k):
    def superDigit_memo(n, k,memo={}):
        # Write your code here
        if n in memo:
            return memo[n]
        
        if len(str(n))==1:
            return n
        #123 123==(123)*2
        print("N=",n,"k=",k)
        #newn=str(n)*int(k)
        result= sum([int(i) for i in str(n)])*k
        if (len(str(result)))>1:
            memo[n]=superDigit_memo(result,1,memo) 
            return memo[n]
        else:
            memo[n]=result
            return result
        
    return superDigit_memo(n,k)

print(superDigit(n,k))



def isBalanced(s):
    # Write your code here
    openingbr=["(","{","["]
    closingbr=[")","}","]"]
    quebala=[]
    for i in s:
        if not quebala:
            quebala.append(i)
        else:
            if i in  openingbr:
                quebala.append(i)
            else: 
                ipos=closingbr.index(i)
                iopen=openingbr[ipos]
                if quebala[-1]!=iopen:
                    return "NO"
                else:
                    quebala.pop()
                #closing
    if quebala:
        return "NO"
                    
    return "YES" 

# 
# 
# 
print(isBalanced("{(([])[])[]}"))
print(isBalanced("{(([])[])[]]}"))
print(isBalanced("{(([])[])[]}[]"))