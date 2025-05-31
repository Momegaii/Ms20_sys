const nodes = document.querySelectorAll('.node');
const title = document.getElementById('infoTitle');
const text = document.getElementById('infoText');

nodes.forEach(node => {
  node.addEventListener('mouseenter', () => {
      const label = node.querySelector('.node-label').textContent;
      const desc = node.querySelector('.node-description').textContent;
      title.textContent = label;
      text.textContent = desc;
    });

   node.addEventListener('mouseleave', () => {
        title.textContent = 'Welcome';
        text.textContent = 'Hover over a node to see details.';
      });
});