-- Used to call the other guy with a 0
iterativeSearch :: (Eq a) => [a] -> a -> Maybe Int

iterativeSearch [] _ = Nothing
iterativeSearch xs val = searchMeat xs val 0

-- Does the search by cutting off the list. Returns
-- Nothing if it is not found
searchMeat :: (Eq a) => [a] -> a -> Int -> Maybe Int

searchMeat (x:xs) val i
 | x == val  = Just i
 | otherwise = searchMeat xs val (i+1)
searchMeat [] _ _ = Nothing

-- Some testing
main = print ([ i | let x = [1, 2, 3, 4, 5, 6, 7], u <- x, let i = iterativeSearch x u])
