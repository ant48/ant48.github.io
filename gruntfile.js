module.exports = function(grunt) {

    // 1. All configuration goes here
    grunt.initConfig({
        //pkg: grunt.file.readJSON('package.json'),

        responsive_images: {
            // 2. Configuration for responsive_images:
            dev: {
              options: {
                engine: 'im',
                sizes: [{
                  width: 800,
                  suffix: '_large',
                  quality: 90
                }, {
                  name: 'small', width: 320
                }, {
                  name: 'medium', width: 640
                }]
              },

              files: [{
                expand: true,
                src: ['*.{gif,jpg,jpeg,png}'],
                cwd: 'img/',
                dest: 'images/'
              }]
            }
          },

          //clear out the images dir if it exists
          clean: {
            dev: {
              src: ['images'],
            },
          },

          //generate images dir if it is missing
          mkdir: {
            dev: {
              options: {
                create: ['images']
              },
            },
          },

    });

    // 3. Where we tell Grunt we plan to use this plug-in.
    grunt.loadNpmTasks('grunt-responsive-images');
    grunt.loadNpmTasks('grunt-contrib-clean');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-mkdir');

    // 4. Where we tell Grunt what to do when we type "grunt" into the terminal.
    grunt.registerTask('default', ['clean', 'mkdir', 'responsive_images']);

};
