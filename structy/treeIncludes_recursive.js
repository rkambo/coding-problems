const treeIncludes = (root, target) => {
  if (root === null) {
    return false;
  }
  if (root.val === target) {
    return true;
  }

  const leftSubTree = treeIncludes(root.left, target);
  const rightSubTree = treeIncludes(root.right, target);

  return leftSubTree || rightSubTree;
};
