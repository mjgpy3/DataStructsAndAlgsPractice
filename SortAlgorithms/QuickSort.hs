quickSort :: (Ord a) => [a] -> [a]

quickSort [] = []

quickSort (x:xs) = quickSort less ++ [x] ++ quickSort greater
 where less = [e | e <- xs, e < x]
       greater = [e | e <- xs, e >= x]

main = print ( quickSort [1, 5, 2, 7, 2, 71, 1, 61] )
