# 哈希冲突与解决方法 / Hash Collisions and Resolution Strategies

> 材料时间 / Material dates：2026-10-29 至 2026-11-02 的学习对话整理，不是课堂原始记录。入口见 [[Courses/2026_fall/recent_learning_review]]。  
> Organized from study conversations dated 2026-10-29 to 2026-11-02; this is not an original class transcript.

## 问题与直觉 / Problem and Intuition

哈希表用哈希函数把键直接算成数组下标，理想情况下查找只需一步。但表的位置有限，不同的键会算出同一个下标，这叫哈希冲突（collision）。冲突无法完全避免，关键是“撞了之后放哪里、以后怎么找回来”。

A hash table computes an array index directly from a key, so a lookup ideally takes one step. Slots are limited, so different keys can map to the same index; this is a collision. Collisions cannot be avoided entirely; the question is where to put the colliding key and how to find it later.

例：$m=11$，$h(k)=k\bmod11$。键 $14,25,36,47$ 的余数都是 $3$。

Example: with $m=11$ and $h(k)=k\bmod11$, the keys $14,25,36,47$ all hash to $3$.

## 两大类方法 / Two Families of Methods

**链地址法（chaining）**：每个桶挂一个链表，同一下标的元素都放进这条链。冲突不占用其他桶；装载因子可以大于 $1$。

**Chaining:** each bucket holds a linked list, and all keys with the same index go into that list. Collisions never occupy other buckets, and the load factor may exceed $1$.

**开放寻址（open addressing）**：所有元素都放在表内；目标位置被占用时，按固定规则依次探测（probe）其他位置。第 $i$ 次探测（$i=0,1,2,\dots$）的位置：

**Open addressing:** every key lives in the table itself; when the home slot is occupied, probe other slots by a fixed rule. The $i$-th probe position for $i=0,1,2,\dots$ is:

| 方法 / Method | 位置 / Position | 偏移 / Offsets | 特点 / Behavior |
| --- | --- | --- | --- |
| 线性探测 / Linear | $(h(k)+i)\bmod m$ | $0,1,2,3,\dots$ | 简单，但形成连续占用块（主聚集）/ Simple; causes primary clustering |
| 二次探测 / Quadratic | $(h(k)+i^2)\bmod m$ | $0,1,4,9,\dots$ | 跳着走，减轻主聚集 / Jumps; reduces primary clustering |
| 双重哈希 / Double | $(h(k)+i\cdot h_2(k))\bmod m$ | $0,d,2d,\dots$ | 步长随键变化，减轻次聚集 / Key-dependent step; reduces secondary clustering |

- 二次探测每次都从**原始位置** $h(k)$ 加 $i^2$，不是在上一次位置上加。  
  Quadratic probing always adds $i^2$ to the original home position, not to the previous probe.
- **主聚集**：线性探测让占用区连成一片，越长越容易再被撞上。  
  **Primary clustering:** linear probing makes occupied runs merge and grow.
- **次聚集**：初始位置相同的键在二次探测下走完全相同的探测序列。双重哈希让步长依赖键，从而避免这一点。  
  **Secondary clustering:** keys with the same home slot follow the same quadratic sequence; double hashing avoids this with a key-dependent step.
- 二次探测不保证访问所有位置；常用的充分条件是表长 $m$ 为质数且装载因子小于 $\frac12$，此时一定能找到空位。  
  Quadratic probing may not visit every slot; with prime $m$ and load factor below $\frac12$, an empty slot is guaranteed.
- 开放寻址删除元素时不能直接清空，否则会截断其他键的探测链；通常用“已删除”标记。  
  Deleting in open addressing cannot simply empty the slot, or later probe chains break; a deleted marker is used.

## 装载因子与比较次数 / Load Factor and Expected Comparisons

装载因子 $L=\frac{n}{m}$（元素数 / 表长）。$L$ 越大，冲突越多。线性探测成功查找的期望比较次数近似为

The load factor is $L=n/m$. Larger $L$ means more collisions. For a successful search with linear probing, the expected number of comparisons is approximately

$$c=\frac12\left(1+\frac{1}{1-L}\right).$$

**例**：$10036$ 个元素、表长 $98285$。$L=\frac{10036}{98285}\approx0.102$，$c=\frac12\left(1+\frac1{0.898}\right)\approx1.057\approx1.06$。表只占约 $10\%$，平均略多于一次比较就能找到。（按 $L\approx0.10$ 取整代入也得 $1.06$。）

**Example:** With $10036$ items in a table of size $98285$, $L\approx0.102$ and $c\approx1.06$. The table is only about $10\%$ full, so a search needs just over one comparison on average. Rounding $L$ to $0.10$ also gives $1.06$.

## 完整例题：同一组键的四种放法 / Worked Example: Four Strategies on the Same Keys

依次插入 $14,25,36,47$ 到空表，$m=11$，$h(k)=k\bmod11$，所有键的 $h(k)=3$。双重哈希使用自拟的 $h_2(k)=7-(k\bmod7)$。

Insert $14,25,36,47$ in order into an empty table with $m=11$; every key has home slot $3$. Double hashing uses the assumed second hash $h_2(k)=7-(k\bmod7)$.

| 键 / Key | 链地址 / Chaining | 线性 / Linear | 二次 / Quadratic | 双重 / Double |
| --- | --- | --- | --- | --- |
| 14 | 桶 3 / bucket 3 | 3 | 3 | 3 |
| 25 | 桶 3 链尾 / bucket 3 | 4 | $3+1=4$ | $h_2=3$：$3+3=6$ |
| 36 | 桶 3 链尾 / bucket 3 | 5 | $3,4$ 已占 → $3+4=7$ | $h_2=6$：$3+6=9$ |
| 47 | 桶 3 链尾 / bucket 3 | 6 | $3,4,7$ 已占 → $(3+9)\bmod11=1$ | $h_2=2$：$3+2=5$ |

观察：线性探测占满 $3$–$6$ 一整段；二次探测分散到 $3,4,7,1$；双重哈希中每个键的步长不同，第一次探测就各自找到空位。

Observation: linear probing fills the run $3$ to $6$; quadratic probing scatters keys to $3,4,7,1$; double hashing gives each key its own step, so each finds a free slot on the first probe after its home slot.

## 易错点 / Common Mistakes

- 二次探测在上一次位置上累加 $i^2$：应始终从 $h(k)$ 出发。  
  Accumulating $i^2$ from the previous probe instead of from $h(k)$.
- 忘记取模，下标越界。  
  Forgetting the modulus, which produces out-of-range indices.
- 把“链表 + 同一下标”的题选成开放寻址：看到 linked list 就是 chaining。  
  Choosing open addressing when the question describes a linked list at one index; that is chaining.

## 关联笔记 / Related Notes

- [[CMPSC/6.Hash_Tables_and_Graphs/README]] — 本章学习顺序 / Study order for this chapter
- [[Courses/2026_fall/cmpsc_132/files/course_schedule]] — Module 6.2：哈希表与图 / Module 6.2: hash tables and graphs

## 来源 / Sources

- ChatGPT 对话 / ChatGPT conversation：[拓扑排序条件](https://chatgpt.com/c/6ae80de1-096c-832b-bb52-ff09779727cd) — 实际可用内容为二次探测、链地址法、装载因子与 BFS，未包含拓扑排序 / The available content covers quadratic probing, chaining, load factor, and BFS, not topological sort.
- ChatGPT 对话 / ChatGPT conversation：[Quiz Page Viewing](https://chatgpt.com/c/6ae810e7-7154-832e-b44a-fd953704cfe3) — 测验中线性、二次、双重哈希填表；题面未包含，本页不复述答案 / A quiz table on linear, quadratic, and double hashing; the question was not included, so its answers are not reproduced.

[//begin]: # "Autogenerated link references for markdown compatibility"
[//end]: # "Autogenerated link references"
