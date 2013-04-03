using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace List_DSA
{
    class List
    {
        private Node _root;

        public List()
        {
            _root = null;
        }

        public Node Search(Object sought)
        {
            Node current = _root;
            
            while (current != null)
            {
                if (sought.ToString() == current.Data.ToString())
                    return current;

                current = current.Next;
            }

            return null;
        }

        public void Insert(Object addMe)
        {
            Node toAttach = new Node();     // Construct the new node
            toAttach.Data = addMe;

            if (_root == null)
            {
                _root = toAttach;
            }
            else
            {
                Node rest = _root;
                _root = toAttach;
                _root.Next = rest;
            }
        }

        public void Delete(Object deleteMe)
        {
            if (deleteMe.ToString() == _root.Data.ToString())
            {
                _root = _root.Next;
                return;
            }

            Node current = _root;

            while (current.Next != null)
            {
                if (current.Next.Data.ToString() == deleteMe.ToString())
                {
                    current.Next = current.Next.Next;
                    return;
                }

                current = current.Next;
            }
        }

        public override string ToString()
        {
            return _root.ToString();
        }
    }
}
