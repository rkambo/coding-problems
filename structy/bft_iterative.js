const breadthFirstValues = (root) => {
  queue = [root];
  if (root === null) {
    return [];
  }
  arr = [];
  while (queue.length > 0) {
    const current = queue.shift();
    arr.push(current.val);
    if (current.left) {
      queue.push(current.left);
    }
    if (current.right) {
      queue.push(current.right);
    }
  }
  return arr;
};
