odoo.define('theme_example.s_container_3d_frontend', function(require) {
  'use strict';

  var sAnimation = require('website.content.snippets.animation');
  sAnimation.registry.container3d = sAnimation.Class.extend({
    selector: '.container-3d',
    start: function() {
      var self = this;

      var camera, scene, renderer;
      var mesh;
      init();
      animate();

      function init() {
        self.$el.find('canvas').remove()
        camera = new THREE.PerspectiveCamera(70, self.$el.innerWidth() / self.$el.innerHeight(), 1, 1000);
        camera.position.z = 400;
        scene = new THREE.Scene();
        var texture = new THREE.TextureLoader().load('/theme_example/static/src/img/crate.gif');
        var geometry = new THREE.BoxBufferGeometry(200, 200, 200);
        var material = new THREE.MeshBasicMaterial({
          map: texture
        });
        mesh = new THREE.Mesh(geometry, material);
        scene.add(mesh);
        renderer = new THREE.WebGLRenderer({
          antialias: true
        });
        renderer.setPixelRatio(window.devicePixelRatio);

        renderer.setSize(self.$el.innerWidth(), self.$el.innerHeight());

        self.$el.append(renderer.domElement);
        //
        window.addEventListener('resize', onWindowResize, false);
      }

      function onWindowResize() {
        camera.aspect = self.$el.innerWidth() / self.$el.innerHeight();
        camera.updateProjectionMatrix();
        renderer.setSize(self.$el.innerWidth(), self.$el.innerHeight());
      }

      function animate() {
        requestAnimationFrame(animate);
        mesh.rotation.x += 0.005;
        mesh.rotation.y += 0.01;
        renderer.render(scene, camera);
      }
      return this._super.apply(this, arguments);
    }
  });

});
