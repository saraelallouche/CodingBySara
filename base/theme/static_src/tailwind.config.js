/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */
module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
    extend: {
        colors: {
            primary: {
                50: '#F4F4F4',   // Couleur très claire
                100: '#D9D9D9',
                200: '#BFBFBF',
                300: '#A6A6A6',
                400: '#8C8C8C',
                500: '#737373',   // Couleur de base
                600: '#595959',
                700: '#404040',
                800: '#262626',
                900: '#1A1A1A',   // Couleur très sombre
                950: '#121212',
            },
            secondary: {
                DEFAULT:'#FFFFFF',
                50: '#FFFFFF',    // Couleur très claire
                100: '#F2F2F2',
                200: '#E6E6E6',
                300: '#D9D9D9',
                400: '#CCCCCC',
                500: '#BFBFBF',   // Couleur de base
                600: '#A3A3A3',
                700: '#888888',
                800: '#6D6D6D',
                900: '#525252',   // Couleur sombre
                950: '#393939',
            },
            accent: {
                50: '#F3E6F9',   // Couleur très claire
                100: '#D39BDF',
                200: '#AA70D4',
                300: '#7A35C6',
                400: '#5000A6',
                500: '#6A0DAD',   // Couleur de base
                600: '#5A0B97',
                700: '#4A087F',
                800: '#3A0567',
                900: '#2A034F',   // Couleur sombre
                950: '#1A0237',
            },
            secondary_accent: {
                50: '#E0FFFF',   // Couleur très claire
                100: '#B3F0FF',
                200: '#80E0FF',
                300: '#4DCFFF',
                400: '#1ABFDF',
                500: '#00BFFF',   // Couleur de base
                600: '#00A3D9',
                700: '#0088B3',
                800: '#006E8C',
                900: '#005266',   // Couleur sombre
                950: '#003B3F',
            },
            detail: {
                50: '#E6E6E6',   // Couleur très claire
                100: '#D1D1D1',
                200: '#A6A6A6',
                300: '#808080',
                400: '#595959',
                500: '#B0B0B0',   // Couleur de base
                600: '#999999',
                700: '#7F7F7F',
                800: '#666666',
                900: '#4D4D4D',   // Couleur sombre
                950: '#333333',
            },
        },
    },
},

    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
