const depthFirstValues = (root) => {
  if (root === null) {
    return [];
  }
  const leftSubtree = depthFirstValues(root.left);
  const rightSubtree = depthFirstValues(root.right);

  return [root.val, ...leftSubtree, ...rightSubtree];
};
