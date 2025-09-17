# The Nth Tibonacci Number

## Subject

泰波那契序列 $$T_n$$ 定义如下： 

$$T_0 = 0$$, $$T_1$$ = 1, $$T_2$$ = 1, 且在 n >= 0 的条件下 $$T_{n+3} = Tn + T_{n+1} + T_{n+2}$$

给你整数 `n`，请返回第 `n` 个泰波那契数 $$T_n$$ 的值。

**<span style = "color:blue">example</span>**

<span style = "color:blue">example1：</span>

> ```markdown
> 输入：n = 4
> 输出：4
> 解释：
> T_3 = 0 + 1 + 1 = 2
> T_4 = 1 + 1 + 2 = 4
> ```

<span style = "color:blue">example2：</span>

> ```markdown
> 输入：n = 25
> 输出：1389537
> ```

**<span style = "color:green">Prompt</span>**

- `0 <= n <= 37`
- 答案保证是一个 32 位整数，即 `answer <= 2^31 - 1`。

## Dynamic programming

**<span style="color:red">Code</span>**

```Python
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        Q, K, V = 0, 1, 1
        for _ in range(3, n+1):
            Q, K, V = K, V, Q + K + V
        return V

solu = Solution()
print(solu.tribonacci(n = 7))
```

**<span style="color:brown">Thought</span>**

泰波那契数的边界条件是 $$T(0)=0,T(1)=1,T(2)=1$$。当 $$n>2$$ 时，每一项的和都等于前三项的和，因此有如下递推关系：

$$T(n)=T(n−1)+T(n−2)+T(n−3)$$
由于泰波那契数存在递推关系，因此可以使用动态规划求解。动态规划的状态转移方程即为上述递推关系，边界条件为 $$T(0)、T(1)$$ 和 $$T(2)$$。

根据状态转移方程和边界条件，可以得到时间复杂度和空间复杂度都是 $$O(n)$$ 的实现。由于 $$T(n)$$ 只和前三项有关，因此可以使用「滚动数组思想」将空间复杂度优化成 $$O(1)$$。

**<span style="color:green">Complexity analysis</span>**

- 时间复杂度：$$O(n)$$
- 空间复杂度：$$O(1)$$

## Fast power of matrix


