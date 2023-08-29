const maxPathSum = (root) => {
  if (root === null) {
    return -Infinity;
  }
  if (root.left === null && root.right === null) {
    return root.val;
  }
  const leftMax = maxPathSum(root.left);
  const rightMax = maxPathSum(root.right);

  return root.val + Math.max(leftMax, rightMax);
};

module.exports = {
  maxPathSum,
};
