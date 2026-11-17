# Arrays — Complete Theory Guide (Basic → Advanced)
### Based on your Array Notes (Striver's A2Z Sheet) — 12 Easy, 8 Medium, 9 Hard

---

## PART 0 — FOUNDATIONS (read this first, everything else builds on it)

### 0.1 What actually is an array?
An array is a **contiguous block of memory**. If `arr` starts at address `1000` and each `int` takes 4 bytes, then `arr[i]` lives at address `1000 + 4*i`. This is *why* `arr[i]` is O(1) — it's pure arithmetic, no searching involved.

Consequences that explain almost every array trick you'll ever see:
- **Access by index** → O(1)
- **Insert/Delete at the end** → O(1) (usually)
- **Insert/Delete at the start or middle** → O(n) — everything after has to shift
- **Search (unsorted)** → O(n)
- **Search (sorted)** → O(log n) via binary search

### 0.2 The five "master patterns" that solve 90% of array problems
Almost every question in your notes is one of these five ideas wearing a costume:

1. **Two Pointers** — two indices moving toward each other or in the same direction. Used when the array is sorted or you need pairs/triplets.
2. **Prefix Sum** — precompute running totals so range-sum queries become O(1) subtraction. Used when you keep needing "sum from i to j."
3. **Hashing (HashMap/HashSet)** — trade space for speed. "Have I seen this before?" in O(1).
4. **Kadane's Algorithm** — a specific greedy/DP trick for "best contiguous subarray" problems.
5. **Sort first, then scan** — many problems become trivial once sorted, at the cost of O(n log n).

Keep these five in your head. When you read a new problem, ask "which of these five does this smell like?"

### 0.3 Two Pointers — the idea
If the array is sorted, and you're looking for a pair/combination that satisfies some sum condition, put one pointer at the start (`i`) and one at the end (`j`):
- If `arr[i] + arr[j] > target` → the sum is too big → decrease it → move `j` left (smaller number)
- If `arr[i] + arr[j] < target` → the sum is too small → increase it → move `i` right
- If equal → found it

**Why does this work and not miss answers?** Because the array is sorted, moving `j` left is the *only* way to decrease the sum without losing any candidate pair — every pair with the old `j` and any `i' > i` would be even bigger, so we've safely eliminated them all in one step. This is the core reason Two Pointers achieves O(n) instead of the O(n²) brute force of checking every pair.

### 0.4 Kadane's Algorithm — the idea
**Problem it solves:** find the maximum sum of any contiguous subarray.

**Core insight:** As you walk through the array keeping a running `sum`, if that running sum ever goes negative, it can only *hurt* any future subarray it's attached to. So the moment `sum < 0`, throw it away and restart from 0. At every step, record the best `sum` seen so far — that's your answer.

Think of it like a football team's momentum: negative momentum should never be "carried forward" into the next play; you reset and start fresh.

### 0.5 XOR trick — the idea
Two properties of XOR make it powerful:
- `x ^ x = 0` (a number cancels itself)
- `x ^ 0 = x`, and XOR is commutative/associative (order doesn't matter)

So if every number in an array appears **exactly twice** except one number which appears **once**, XOR-ing everything together cancels all the pairs, leaving only the lonely number. No extra space needed — this beats hashing.

### 0.6 Moore's Voting Algorithm — the idea
**Problem it solves:** find the element that appears more than `n/2` times (a true majority).

**Core insight:** think of it like a boxing match. Keep a `candidate` and a `count`. Every time you see the same element, count++; every time you see a different one, count--. If count hits 0, the current element "loses" and the next element becomes the new candidate. Because the majority element appears more than half the time, it can survive any number of "knockouts" from minority elements and will be left standing at the end.

**Important:** this only *guarantees* a majority if one is proven to exist (>n/2 times). Otherwise you must re-verify by counting the candidate's actual frequency — that's why your notes say "always check >N/2 condition."

### 0.7 Dutch National Flag Algorithm — the idea
**Problem it solves:** sort an array containing only 0s, 1s, and 2s — in a single pass, O(1) space.

**Core insight:** maintain three regions using three pointers `low`, `mid`, `high`:
- `[0, low)` → all 0s (already placed)
- `[low, mid)` → all 1s (already placed)
- `[mid, high]` → unknown, still being processed
- `(high, n-1]` → all 2s (already placed)

Walk `mid` through the unknown region:
- If `arr[mid] == 0` → swap with `low`, then `low++, mid++` (0 correctly placed, move on)
- If `arr[mid] == 1` → it's already in the right zone, just `mid++`
- If `arr[mid] == 2` → swap with `high`, then `high--` (do **not** move `mid` — the swapped-in element from `high` hasn't been checked yet)

This is exactly the flag colors of the Dutch flag (red, white, blue) sorted in place — hence the name.

### 0.8 Prefix Sum — the idea
Define `prefix[i] = arr[0] + arr[1] + ... + arr[i]`. Then the sum of any subarray `arr[i..j]` is just `prefix[j] - prefix[i-1]` — O(1) per query after O(n) preprocessing.

Combined with a **HashMap of {prefix_sum → count/index}**, this becomes extremely powerful for "subarray with sum = k" type problems, because you're really asking: "has some earlier prefix sum equal to `current_sum - k`?"

### 0.9 Merge Sort as a counting tool
Merge Sort doesn't just sort — while merging two sorted halves, you get a free opportunity to **count cross-pairs** that satisfy some condition (inversions, reverse pairs, etc.), because both halves are already sorted, so counting becomes arithmetic instead of nested loops. This is why 3 of your 9 hard problems are "merge sort in disguise."

---

## PART 1 — EASY (12 Questions)

### Q1. Largest element in an array
**Idea:** Track the max as you scan once.
**Why it works:** at any point, `max` holds the largest of everything seen *so far* — by induction, after the full scan it holds the largest of everything.
**Complexity:** O(n) time, O(1) space.

```cpp
int largestElement(vector<int>& arr) {
    int maxVal = INT_MIN;              // start impossibly small
    for (int i = 0; i < arr.size(); i++) {
        maxVal = max(maxVal, arr[i]);  // update if current element is bigger
    }
    return maxVal;
}
```

---

### Q2. Kth smallest / largest element
**Idea (brute, matches your notes):** sort the array; for kth smallest, answer is `arr[k-1]`; for kth largest, `arr[n-k]`.
**Why:** after sorting ascending, the smallest is at index 0, so the kth smallest is naturally at index `k-1`.
**Complexity:** O(n log n) due to sort. (An optimal O(n) average approach exists using **QuickSelect**, and O(n log k) using a heap — worth learning next as an upgrade.)

```cpp
int kthSmallest(vector<int> arr, int k) {
    sort(arr.begin(), arr.end());
    return arr[k - 1];
}

int kthLargest(vector<int> arr, int k) {
    sort(arr.begin(), arr.end());
    return arr[arr.size() - k];
}
```

---

### Q3. Check if array is sorted
**Idea:** In a sorted array, every element must be ≥ the one before it. One violation breaks it.
**Complexity:** O(n) time, O(1) space.

```cpp
bool isSorted(vector<int>& arr) {
    for (int i = 1; i < arr.size(); i++) {
        if (arr[i - 1] > arr[i]) return false;  // found a decrease -> not sorted
    }
    return true;
}
```

---

### Q4 & Q5. Left/Right Rotate an array by K places
**Core trick — the "reversal algorithm":** Reversing sub-parts of an array is a clean way to rotate it without extra space.

**Left rotate by k:**
1. Reverse `[0, k-1]`
2. Reverse `[k, n-1]`
3. Reverse the whole array `[0, n-1]`

**Right rotate by k:** exact mirror —
1. Reverse the whole array `[0, n-1]`
2. Reverse `[0, k-1]`
3. Reverse `[k, n-1]`

**Intuition for why this works:** Reversing the whole array flips everything, and then re-reversing chunks "un-flips" only the internal order of each chunk while keeping the chunk's new *position* — the net effect is a rotation. Trace it on paper once with `[1,2,3,4,5]`, k=2 and it'll click permanently.

**Complexity:** O(n) time, O(1) extra space — this is the elegant part; naive approaches use O(k) or O(n) extra space with a temp array.

```cpp
void reverse(vector<int>& a, int i, int j) {
    while (i < j) {
        swap(a[i], a[j]);
        i++; j--;
    }
}

void leftRotate(vector<int>& a, int k) {
    int n = a.size();
    k = k % n;                  // handle k > n
    reverse(a, 0, k - 1);
    reverse(a, k, n - 1);
    reverse(a, 0, n - 1);
}

void rightRotate(vector<int>& a, int k) {
    int n = a.size();
    k = k % n;
    reverse(a, 0, n - 1);
    reverse(a, 0, k - 1);
    reverse(a, k, n - 1);
}
```

---

### Q6. Move zeroes to the end
**Idea (the "snowball" technique):** Keep a variable `j` marking the next position to place a non-zero. Walk through with `i`; whenever `arr[i] != 0`, swap it into position `j` and advance `j`. Everything after gets naturally filled with zeros because you only ever pull non-zeros forward.
**Complexity:** O(n) time, O(1) space, and it preserves relative order — a nice bonus of this technique.

```cpp
void moveZeroes(vector<int>& a) {
    int j = 0;                          // next slot for a non-zero element
    for (int i = 0; i < a.size(); i++) {
        if (a[i] != 0) {
            swap(a[i], a[j]);
            j++;
        }
    }
}
```

---

### Q7. Union of 2 sorted arrays
**Idea:** Classic merge-sort-style two pointers. Walk both arrays simultaneously, always taking the smaller element next, and only add it if it's different from the last element added (to avoid duplicates).
**Complexity:** O(n + m) time.

```cpp
vector<int> unionArrays(vector<int>& a, vector<int>& b) {
    int n = a.size(), m = b.size();
    vector<int> ans;
    int i = 0, j = 0;
    while (i < n && j < m) {
        int val;
        if (a[i] <= b[j]) { val = a[i]; i++; }
        else              { val = b[j]; j++; }
        if (ans.empty() || ans.back() != val) ans.push_back(val);
    }
    while (i < n) {
        if (ans.empty() || ans.back() != a[i]) ans.push_back(a[i]);
        i++;
    }
    while (j < m) {
        if (ans.empty() || ans.back() != b[j]) ans.push_back(b[j]);
        j++;
    }
    return ans;
}
```

---

### Q8. Intersection of 2 sorted arrays
**Idea:** Same two-pointer walk, but only add an element when both pointers point at equal values (meaning it exists in both arrays), then advance both.
**Complexity:** O(n + m) time.

```cpp
vector<int> intersectionArrays(vector<int>& a, vector<int>& b) {
    vector<int> ans;
    int i = 0, j = 0;
    while (i < a.size() && j < b.size()) {
        if (a[i] < b[j]) i++;
        else if (a[i] > b[j]) j++;
        else { ans.push_back(a[i]); i++; j++; }  // match found
    }
    return ans;
}
```

---

### Q9. Find missing number in an array (1 to n, one missing)
**Idea:** The sum of `1..n` is `n*(n+1)/2`. Subtract the actual sum of the array from this — what's left over is the missing number.
**Alternative:** XOR trick works too (XOR 1..n and XOR all array elements; XOR the two results).
**Complexity:** O(n) time, O(1) space.

```cpp
int findMissingNumber(vector<int>& a, int n) {
    long long expectedSum = (long long)n * (n + 1) / 2;
    long long actualSum = 0;
    for (int x : a) actualSum += x;
    return (int)(expectedSum - actualSum);
}
```

---

### Q10. Find the number that appears once (all others appear twice)
**Idea:** Pure XOR trick from Section 0.5. XOR every element together — pairs cancel out, the lone survivor remains.
**Complexity:** O(n) time, O(1) space — better than a HashMap approach which would need O(n) space.

```cpp
int singleNumber(vector<int>& a) {
    int ans = 0;
    for (int x : a) ans ^= x;
    return ans;
}
```

---

### Q11. Longest subarray with given sum K
**Idea:** Prefix sum + HashMap (Section 0.8). As you scan and keep a running `sum`, check: has `sum - k` occurred as a prefix sum before? If yes, the subarray between that earlier index and now sums to exactly k. Track the max length. **Only store the first occurrence** of each prefix sum in the map — you want the *earliest* index to maximize length.
**Complexity:** O(n) time, O(n) space.

```cpp
int longestSubarrayWithSumK(vector<int>& a, int k) {
    unordered_map<int, int> firstIndex;   // prefix sum -> earliest index where it occurred
    int sum = 0, len = 0;
    for (int i = 0; i < a.size(); i++) {
        sum += a[i];
        if (sum == k) len = max(len, i + 1);       // subarray from start
        int remainder = sum - k;
        if (firstIndex.count(remainder)) {
            len = max(len, i - firstIndex[remainder]);
        }
        if (!firstIndex.count(sum)) firstIndex[sum] = i;  // store only first occurrence
    }
    return len;
}
```

---

### Q12. Sort an array of 0s, 1s, and 2s
**Idea:** Direct application of the Dutch National Flag algorithm from Section 0.7.
**Complexity:** O(n) time, single pass, O(1) space — beats a generic sort's O(n log n).

```cpp
void sortColors(vector<int>& a) {
    int low = 0, mid = 0, high = a.size() - 1;
    while (mid <= high) {
        if (a[mid] == 0) {
            swap(a[low], a[mid]);
            low++; mid++;
        } else if (a[mid] == 1) {
            mid++;
        } else {  // a[mid] == 2
            swap(a[mid], a[high]);
            high--;   // don't increment mid — recheck swapped-in value
        }
    }
}
```

---

## PART 2 — MEDIUM (8 Questions)

### Q1. Majority element (appears > n/2 times)
**Idea:** Moore's Voting Algorithm (Section 0.6). Then re-verify the candidate actually appears > n/2 times.
**Complexity:** O(n) time, O(1) space — much better than sorting (O(n log n)) or hashing (O(n) space).

```cpp
int majorityElement(vector<int>& a) {
    int count = 0, candidate = 0;
    for (int x : a) {
        if (count == 0) { candidate = x; count = 1; }
        else if (x == candidate) count++;
        else count--;
    }
    // verification pass (important! candidate might be wrong if no true majority exists)
    int freq = 0;
    for (int x : a) if (x == candidate) freq++;
    if (freq > a.size() / 2) return candidate;
    return -1;  // no majority element exists
}
```

---

### Q2. Maximum subarray sum
**Idea:** Kadane's Algorithm (Section 0.4) — direct application.
**Complexity:** O(n) time, O(1) space.

```cpp
int maxSubArraySum(vector<int>& a) {
    int maxSum = INT_MIN, sum = 0;
    for (int x : a) {
        sum += x;
        maxSum = max(maxSum, sum);
        if (sum < 0) sum = 0;   // negative sum only hurts future — reset
    }
    return maxSum;
}
```

---

### Q3. Print next permutation
**Idea:** This is about understanding how permutations are ordered lexicographically.
1. Scan from the right, find the first index `i` where `nums[i] < nums[i+1]` — this is the "breakpoint" (the point where the sequence stops decreasing from the right).
2. If no such index exists, the array is the last permutation (fully descending) — reverse it entirely to get the first permutation.
3. Otherwise, scan from the right again to find the smallest element greater than `nums[i]`, swap them.
4. Reverse everything after index `i` (it was descending, and reversing makes it the smallest possible arrangement — giving the *next* permutation, not some far-later one).

**Why this works:** to get the *next* permutation, you want the smallest possible increase. The breakpoint identifies the rightmost place you can "bump up" a digit; swapping in the smallest larger digit and then sorting (via reverse, since it's already descending) the remainder ascending gives the minimal next arrangement.

**Complexity:** O(n) time, O(1) space.

```cpp
void nextPermutation(vector<int>& nums) {
    int n = nums.size();
    int index = -1;
    for (int i = n - 2; i >= 0; i--) {
        if (nums[i] < nums[i + 1]) { index = i; break; }
    }
    if (index == -1) {
        reverse(nums.begin(), nums.end());  // last permutation -> wrap to first
        return;
    }
    for (int i = n - 1; i > index; i--) {
        if (nums[i] > nums[index]) {
            swap(nums[i], nums[index]);
            break;
        }
    }
    reverse(nums.begin() + index + 1, nums.end());
}
```

---

### Q4. Leaders in an array
**Idea:** An element is a "leader" if everything to its right is smaller. The last element is always a leader. Scan **right to left**, tracking the max seen so far — anything greater than that running max is a new leader.
**Complexity:** O(n) time (a naive approach checking every element against everything to its right would be O(n²)).

```cpp
vector<int> leaders(vector<int>& a) {
    int n = a.size();
    vector<int> ans;
    int maxFromRight = a[n - 1];
    ans.push_back(maxFromRight);
    for (int i = n - 2; i >= 0; i--) {
        if (a[i] > maxFromRight) {
            maxFromRight = a[i];
            ans.push_back(a[i]);
        }
    }
    reverse(ans.begin(), ans.end());  // we collected right-to-left, so flip for original order
    return ans;
}
```

---

### Q5 & Q6. Rotate a matrix by 90° (clockwise / anticlockwise)
**Clockwise:**
1. **Transpose** the matrix (flip along the main diagonal: `swap(a[i][j], a[j][i])` for `j > i`)
2. **Reverse each row**

**Anticlockwise:** exact mirror —
1. **Reverse each row** first
2. **Transpose** the matrix

**Intuition:** picture rotating a square photo 90°. Transposing swaps rows and columns (turns it "diagonally"), and reversing rows/flipping finishes the rotation in the right direction. Draw a 3x3 grid with numbers 1-9 and trace both operations by hand once — it makes the direction logic permanent in memory.

**Complexity:** O(n²) time, O(1) extra space — this in-place trick avoids needing a second matrix.

```cpp
void transpose(vector<vector<int>>& a) {
    int n = a.size();
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            swap(a[i][j], a[j][i]);
}

void rotateClockwise(vector<vector<int>>& a) {
    transpose(a);
    for (auto& row : a) reverse(row.begin(), row.end());
}

void rotateAntiClockwise(vector<vector<int>>& a) {
    for (auto& row : a) reverse(row.begin(), row.end());
    transpose(a);
}
```

---

### Q7. Set matrix zeroes
**Problem:** if any cell is 0, set its entire row and column to 0 — but do it **in-place** without extra matrix (O(1) extra space beyond a couple of markers).

**Idea:** Instead of a separate array to mark "which rows/cols to zero," reuse the matrix's own first row and first column as markers:
- `matrix[i][0]` marks whether row `i` should be zeroed
- `matrix[0][j]` marks whether column `j` should be zeroed
- Since `matrix[0][0]` is shared by both, use a separate `extra` variable just for tracking column 0 specially.

**Steps:**
1. Set `extra = 1` (assumes column 0 doesn't need zeroing initially)
2. Scan the matrix; wherever you find a 0, mark its row-start and col-start (or `extra` if column is 0)
3. Scan again **from the bottom-right backwards** (important — so you don't overwrite markers before using them), zeroing any cell whose row-marker or col-marker says so
4. Finally handle column 0 using `extra`

**Complexity:** O(rows × cols) time, O(1) extra space.

```cpp
void setZeroes(vector<vector<int>>& matrix) {
    int rows = matrix.size(), cols = matrix[0].size();
    int extra = 1;  // tracks whether column 0 needs zeroing

    for (int i = 0; i < rows; i++) {
        if (matrix[i][0] == 0) extra = 0;
        for (int j = 1; j < cols; j++) {
            if (matrix[i][j] == 0) {
                matrix[i][0] = 0;   // mark row
                matrix[0][j] = 0;   // mark column
            }
        }
    }

    // apply markers, starting from bottom-right so markers aren't destroyed early
    for (int i = rows - 1; i >= 0; i--) {
        for (int j = cols - 1; j >= 1; j--) {
            if (matrix[i][0] == 0 || matrix[0][j] == 0)
                matrix[i][j] = 0;
        }
        if (extra == 0) matrix[i][0] = 0;
    }
}
```

---

### Q8. Count subarrays with sum K
**Idea:** Prefix sum + HashMap (Section 0.8), but this time counting occurrences instead of tracking first index. `map[0] = 1` is seeded upfront because a prefix sum of exactly `k` by itself (from index 0) must be counted too — that's the "empty prefix before the array" trick.
**Complexity:** O(n) time, O(n) space.

```cpp
int subarraySum(vector<int>& a, int k) {
    unordered_map<int, int> freq;
    freq[0] = 1;                 // empty prefix sum
    int sum = 0, count = 0;
    for (int x : a) {
        sum += x;
        int need = sum - k;
        if (freq.count(need)) count += freq[need];
        freq[sum]++;
    }
    return count;
}
```

---

## PART 3 — HARD (9 Questions)

### Q1. Pascal's Triangle
Pascal's triangle uses combinatorics: the element at row `r`, column `c` (0-indexed) is `C(r, c)` = "r choose c."

**a) Calculate a single element** — `C(n, r)`:
Build it iteratively to avoid factorial overflow: `ans = ans * (n - i) / (i + 1)`.

```cpp
long long nCr(int n, int r) {
    long long ans = 1;
    for (int i = 0; i < r; i++) {
        ans = ans * (n - i);
        ans = ans / (i + 1);
    }
    return ans;
}
```

**b) Generate the nth row:**
Each element is derived from the previous: `next = prev * (n - i) / i`.

```cpp
vector<long long> nthRow(int n) {
    vector<long long> row;
    long long ans = 1;
    row.push_back(1);
    for (int i = 1; i <= n; i++) {
        ans = ans * (n - i + 1);
        ans = ans / i;
        row.push_back(ans);
    }
    return row;
}
```

**c) Generate the full triangle:** simply call "generate nth row" for every row from 0 to n-1.

```cpp
vector<vector<long long>> pascalsTriangle(int numRows) {
    vector<vector<long long>> triangle;
    for (int i = 0; i < numRows; i++) {
        triangle.push_back(nthRow(i));
    }
    return triangle;
}
```

---

### Q2. Majority element (n/3 times) — find elements appearing more than n/3 times
**Idea:** Extended Moore's Voting. Since something appearing >n/3 times means **at most 2 such elements can exist** in the whole array (you can't fit 3 groups each >n/3 into n elements), track **two** candidates and two counters simultaneously.
**Complexity:** O(n) time, O(1) space.

```cpp
vector<int> majorityElementN3(vector<int>& a) {
    int num1 = -1, num2 = -1, c1 = 0, c2 = 0;
    for (int x : a) {
        if (x == num1) c1++;
        else if (x == num2) c2++;
        else if (c1 == 0) { num1 = x; c1 = 1; }
        else if (c2 == 0) { num2 = x; c2 = 1; }
        else { c1--; c2--; }
    }
    // verification pass — candidates might not actually be majority
    c1 = 0; c2 = 0;
    for (int x : a) {
        if (x == num1) c1++;
        else if (x == num2) c2++;
    }
    vector<int> ans;
    int n = a.size();
    if (c1 > n / 3) ans.push_back(num1);
    if (c2 > n / 3) ans.push_back(num2);
    return ans;
}
```

---

### Q3. Merge overlapping sub-intervals
**Idea:** **Sort intervals by start time first** — this is the key setup step that makes everything else trivial. Then walk through: if the current interval's start is ≤ the end of the last merged interval, they overlap — merge by extending the end (`max` of the two ends). Otherwise, push the current interval as a new, separate one.
**Complexity:** O(n log n) for sorting + O(n) for the merge pass.

```cpp
vector<vector<int>> mergeIntervals(vector<vector<int>>& intervals) {
    sort(intervals.begin(), intervals.end());   // sort by start time
    vector<vector<int>> ans;
    for (auto& interval : intervals) {
        if (ans.empty() || ans.back()[1] < interval[0]) {
            ans.push_back(interval);            // no overlap -> new interval
        } else {
            ans.back()[1] = max(ans.back()[1], interval[1]);  // overlap -> merge
        }
    }
    return ans;
}
```

---

### Q4. 3Sum — find all unique triplets that sum to zero
**Idea:** Sort first. Fix one element `i`, then use **two pointers** (`j` from `i+1`, `k` from the end) on the remaining sorted subarray to find pairs summing to `-a[i]`. Skip duplicates at every level (`i`, `j`, and `k`) to avoid duplicate triplets in the answer.
**Complexity:** O(n²) — a huge improvement over the brute-force O(n³) of checking every triplet.

```cpp
vector<vector<int>> threeSum(vector<int> a) {
    sort(a.begin(), a.end());
    vector<vector<int>> ans;
    int n = a.size();
    for (int i = 0; i < n; i++) {
        if (i > 0 && a[i] == a[i - 1]) continue;   // skip duplicate first element
        int j = i + 1, k = n - 1;
        while (j < k) {
            int sum = a[i] + a[j] + a[k];
            if (sum > 0) k--;
            else if (sum < 0) j++;
            else {
                ans.push_back({a[i], a[j], a[k]});
                j++; k--;
                while (j < k && a[j] == a[j - 1]) j++;  // skip duplicate second element
                while (j < k && a[k] == a[k + 1]) k--;  // skip duplicate third element
            }
        }
    }
    return ans;
}
```

---

### Q5. 4Sum
**Idea:** Direct extension of 3Sum — add one more fixed outer loop, then two pointers for the last two. Skip duplicates at all four levels. Use `long long` for the sum to avoid integer overflow when adding four large ints.
**Complexity:** O(n³).

```cpp
vector<vector<int>> fourSum(vector<int> a, int target) {
    sort(a.begin(), a.end());
    int n = a.size();
    vector<vector<int>> ans;
    for (int i = 0; i < n - 3; i++) {
        if (i > 0 && a[i] == a[i - 1]) continue;
        for (int j = i + 1; j < n - 2; j++) {
            if (j > i + 1 && a[j] == a[j - 1]) continue;
            int k = j + 1, l = n - 1;
            while (k < l) {
                long long sum = (long long)a[i] + a[j] + a[k] + a[l];
                if (sum > target) l--;
                else if (sum < target) k++;
                else {
                    ans.push_back({a[i], a[j], a[k], a[l]});
                    k++; l--;
                    while (k < l && a[k] == a[k - 1]) k++;
                    while (k < l && a[l] == a[l + 1]) l--;
                }
            }
        }
    }
    return ans;
}
```

---

### Q6. Merge two sorted arrays without extra space

**Case A — extra space is available at the end of one array** (e.g. `nums1=[1,2,3,0,0,0]`, `nums2=[1,7,8]`):
Fill **from the back** using three pointers — this avoids overwriting values you haven't read yet.

```cpp
void mergeWithSpace(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    int i = m - 1, j = n - 1, k = m + n - 1;
    while (j >= 0) {
        if (i >= 0 && nums1[i] > nums2[j]) nums1[k--] = nums1[i--];
        else nums1[k--] = nums2[j--];
    }
}
```

**Case B — no extra space, two separate arrays must both end up sorted:**
1. Put a pointer `i` at the **end** of array 1 and `j` at the **start** of array 2.
2. While `nums1[i] > nums2[j]`, swap them and move `i` backward, `j` forward.
3. Stop when they no longer violate order (arr1's tail is now ≤ arr2's head).
4. Finally, sort both arrays individually (they're "almost sorted" so this is cheap in practice, though worst case still O(n log n)).

```cpp
void mergeNoSpace(vector<int>& nums1, vector<int>& nums2) {
    int n = nums1.size(), m = nums2.size();
    int i = n - 1, j = 0;
    while (i >= 0 && j < m) {
        if (nums1[i] > nums2[j]) {
            swap(nums1[i], nums2[j]);
            i--; j++;
        } else break;   // no more violations possible once this holds
    }
    sort(nums1.begin(), nums1.end());
    sort(nums2.begin(), nums2.end());
}
```

---

### Q7. Maximum product subarray
**Idea:** Like Kadane's, but trickier because of **negative numbers** — a negative × negative can flip a small product into the largest one. So track **both** a running max product and a running min product at each step (since a very negative min could become the new max after multiplying by another negative).
**Complexity:** O(n) time, O(1) space.

```cpp
int maxProduct(vector<int>& a) {
    int prodMax = a[0], prodMin = a[0], ans = a[0];
    for (int i = 1; i < a.size(); i++) {
        int temp = max({a[i], prodMax * a[i], prodMin * a[i]});
        prodMin = min({a[i], prodMax * a[i], prodMin * a[i]});
        prodMax = temp;
        ans = max(ans, prodMax);
    }
    return ans;
}
```

---

### Q8. Count inversions
**Definition:** an inversion is a pair `(i, j)` where `i < j` but `a[i] > a[j]` — i.e., "out of order" pairs.

**Idea:** Modified Merge Sort. While merging two already-sorted halves, if an element from the right half is smaller than the current element from the left half, then **every remaining element in the left half** also forms an inversion with it (because the left half is sorted, so they're all ≥ current). That's `mid - left + 1` inversions counted in O(1), instead of checking each one individually.
**Complexity:** O(n log n) — massive improvement over the brute-force O(n²) of checking every pair.

```cpp
long long mergeAndCount(vector<int>& a, int low, int mid, int high) {
    vector<int> temp;
    int left = low, right = mid + 1;
    long long count = 0;
    while (left <= mid && right <= high) {
        if (a[left] <= a[right]) {
            temp.push_back(a[left++]);
        } else {
            count += (mid - left + 1);   // key line: count all remaining left-half elements
            temp.push_back(a[right++]);
        }
    }
    while (left <= mid) temp.push_back(a[left++]);
    while (right <= high) temp.push_back(a[right++]);
    for (int i = low; i <= high; i++) a[i] = temp[i - low];
    return count;
}

long long mergeSortAndCount(vector<int>& a, int low, int high) {
    long long count = 0;
    if (low >= high) return count;
    int mid = (low + high) / 2;
    count += mergeSortAndCount(a, low, mid);
    count += mergeSortAndCount(a, mid + 1, high);
    count += mergeAndCount(a, low, mid, high);
    return count;
}
```

---

### Q9. Reverse pairs
**Definition:** a reverse pair is `(i, j)` where `i < j` but `a[i] > 2 * a[j]` — similar to inversions but with the doubled condition.

**Idea:** Same Merge Sort skeleton as Count Inversions, but with two crucial differences:
1. The **counting condition uses `2 * a[right]`**, and because doubling can overflow `int`, cast to `long long`.
2. Counting must be done in a **separate pass before merging** (using a temporary `right` pointer), because once you merge, the sorted order needed for the `2x` comparison is destroyed. This is the subtle part that trips people up — the count-pass and the merge-pass are two distinct loops, not one combined loop like in Count Inversions.

**Complexity:** O(n log n).

```cpp
void mergeReversePairs(vector<int>& a, int low, int mid, int high) {
    vector<int> temp;
    int left = low, right = mid + 1;
    while (left <= mid && right <= high) {
        if (a[left] <= a[right]) temp.push_back(a[left++]);
        else temp.push_back(a[right++]);
    }
    while (left <= mid) temp.push_back(a[left++]);
    while (right <= high) temp.push_back(a[right++]);
    for (int i = low; i <= high; i++) a[i] = temp[i - low];
}

long long countReversePairs(vector<int>& a, int low, int mid, int high) {
    long long count = 0;
    int right = mid + 1;
    for (int i = low; i <= mid; i++) {
        while (right <= high && a[i] > 2LL * a[right]) right++;
        count += (right - (mid + 1));
    }
    return count;
}

long long reversePairsSort(vector<int>& a, int low, int high) {
    long long count = 0;
    if (low >= high) return count;
    int mid = (low + high) / 2;
    count += reversePairsSort(a, low, mid);
    count += reversePairsSort(a, mid + 1, high);
    count += countReversePairs(a, low, mid, high);   // count BEFORE merging (needs sorted halves)
    mergeReversePairs(a, low, mid, high);            // merge AFTER counting
    return count;
}
```

---

## PART 4 — How to actually revise this

1. **Don't memorize code. Memorize the "smell."** When you see a new problem, ask: sorted array + pairs? → Two Pointers. Need range sums repeatedly? → Prefix Sum. "Best contiguous subarray"? → Kadane's. 0/1/2 sorting? → Dutch Flag. Counting pairs across the array with some inequality? → Modified Merge Sort.
2. **Dry-run on paper** with a tiny array (size 4-5) for every technique above before trusting yourself to code it blind — especially Next Permutation, Set Matrix Zeroes, and Reverse Pairs, which are the three most "gotcha"-prone problems in this list.
3. **Re-derive Dutch National Flag and Kadane's from scratch weekly** until you can write them without looking — they're building blocks for a huge number of future problems beyond this sheet (partition problems, DP problems, etc.).
4. **Time yourself** on the Easy set first (should feel automatic within 2 weeks), then Medium, then Hard.

Good luck, Sam — this set covers essentially the entire "array intuition" toolkit you'll reuse throughout DSA. 🚀
