export default {
  transform: {
    "^.+\\.mjs$": "babel-jest", // Transform .mjs files with Babel
    "^.+\\.js$": "babel-jest", // Transform .js files if needed
  },
  testEnvironment: "node", // Use Node.js as the test environment
};
