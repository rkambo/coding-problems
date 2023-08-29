const treeMinValue = (root) => {
  if (root === null) {
    return Infinity;
  }
  const leftTree = treeMinValue(root.left);
  const rightTree = treeMinValue(root.right);

  return Math.min(root.val, leftTree, rightTree);
};
