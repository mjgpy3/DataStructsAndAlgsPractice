using System;
using System.Threading;

namespace ConwaysGameOfLife
{
	class MainClass
	{
		private static string [] _printables = new string [] {" ", "█"};
		
		public static void Main (string[] args)
		{
			bool [,] grid = new bool[20, 50];
			Random a = new Random();
			
			for (int i = 0; i < grid.GetLength(0); i++)
				for (int j = 0; j < grid.GetLength(1); j++)
					grid[i, j] = (a.Next(10) == 1 ? true : false);
			
			for (int c = 0; c < 1000; c++)
			{
				PrintBoard(grid);
				
				for (int i = 0; i < grid.GetLength(0); i++)
					for (int j = 0; j < grid.GetLength(1); j++)
						grid[i, j] = CellLivesNextTurn(grid, i, j);
				
				Thread.Sleep(100);
				Console.Clear();
			}
			
		}
		
		/// <summary>
		/// Prints the board.
		/// </summary>
		/// <param name='board'>
		/// The game's board.
		/// </param>
		public static void PrintBoard(bool [,] board)
		{
			for (int i = 0; i < board.GetLength(0); i++)
			{
				for (int j = 0; j < board.GetLength(1); j++)
					System.Console.Write(_printables[board[i,j] == false ? 0 : 1]);
				
				System.Console.WriteLine();
			}
		}
		
		/// <summary>
		/// Determines whether a given cell lives next turn.
		/// </summary>
		/// <param name='board'>
		/// Board.
		/// </param>
		/// <param name='y'>
		/// Y.
		/// </param>
		/// <param name='x'>
		/// X.
		/// </param>
		public static bool CellLivesNextTurn(bool [,] board, int y, int x)
		{
			int liveNeighbors = GetNumberOfLivesAround(board, y, x);
			
			if (board[y, x] && (liveNeighbors == 3 || liveNeighbors == 2))
				return true;
			if (!board[y, x] && liveNeighbors == 3)
				return true;
			
			return false;
		}
		
		/// <summary>
		/// Gets the number of lives around a specific y, x point.
		/// </summary>
		/// <returns>
		/// The number of lives around.
		/// </returns>
		/// <param name='board'>
		/// The game's board.
		/// </param>
		/// <param name='y'>
		/// The y-coordinate (0th dimension) point to check.
		/// </param>
		/// <param name='x'>
		/// The x-coordinate (1st dimension) point to check.
		/// </param>
		public static int GetNumberOfLivesAround(bool [,] board, int y, int x)
		{
			int count = board[y,x]? -1 : 0;
			
			for (int dy = y-1; dy < y+2; dy++)
				for (int dx = x-1; dx < x+2; dx++)
					if (dy >= 0 && dx >= 0 && dy < board.GetLength(0) && dx < board.GetLength(1))
						if (board[dy, dx])
							count++;
			
			return count;
		}
	}
}
