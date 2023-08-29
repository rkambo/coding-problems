const treeSum = (root) => {
  if (root === null) {
    return 0;
  }
  const queue = [root];
  let totalSum = 0;
  while (queue.length > 0) {
    const current = queue.shift();
    totalSum += current.val;
    if (current.left) {
      queue.push(current.left);
    }
    if (current.right) {
      queue.push(current.right);
    }
  }
  return totalSum;
};
