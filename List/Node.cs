using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace List_DSA
{
    class Node
    {
        public Node Next { set; get; }
        public Object Data { set; get; }

        public Node()
        {
            Next = null;
        }

        public override string ToString()
        {
            return Data.ToString() + " -> " +
                (Next == null ? "NULL" : Next.ToString());
        }
    }
}
