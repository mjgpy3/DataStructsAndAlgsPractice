binarySearch :: Ord a => [a] -> a -> Int -> Int -> Maybe Int

binarySearch l e beg last
 | lookat == e = Just i
 | i == (length l)-1 || i == 0 = Nothing
 | lookat < e = (binarySearch l e i last)
 | lookat > e = (binarySearch l e beg i)
 where i = quot (beg+last) 2
       lookat = l !! i

main = print (binarySearch [1,2,3,4,5,6,7,8] 4 0 8)
