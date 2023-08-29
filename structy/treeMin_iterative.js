const treeMinValue = (root) => {
  if (root === null) {
    return Infinity;
  }
  const queue = [root];
  let minVal = Infinity;
  while (queue.length > 0) {
    const current = queue.shift();
    if (minVal > current.val) {
      minVal = current.val;
    }
    if (current.left) {
      queue.push(current.left);
    }
    if (current.right) {
      queue.push(current.right);
    }
  }
  return minVal;
};
