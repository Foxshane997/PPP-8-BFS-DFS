// BFS Search Algorithm
class TreeNode {
  constructor(val, left = null, right = null) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

function largestValues(root) {
  if (!root) return [];

  let result = [];
  let queue = [root];

  while (queue.length > 0) {
    let levelSize = queue.length;
    let max = -Infinity;

    for (let i = 0; i < levelSize; i++) {
      let node = queue.shift();

      console.log(`Processing node with value: ${node.val}`);

      max = Math.max(max, node.val);

      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }

    result.push(max);
  }

  return result;
}

let root = new TreeNode(5);
root.left = new TreeNode(3);
root.right = new TreeNode(8);
root.left.left = new TreeNode(2);
root.left.right = new TreeNode(4);
root.right.right = new TreeNode(9);

console.log("Largest values in each row:", largestValues(root));
