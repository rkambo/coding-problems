const treeIncludes = (root, target) => {
  const queue = [root];
  if (root === null) {
    return false;
  }
  while (queue.length > 0) {
    const current = queue.shift();
    if (current.val === target) {
      return true;
    }
    if (current.left) {
      queue.push(current.left);
    }
    if (current.right) {
      queue.push(current.right);
    }
  }
  return false;
};
