module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'jsdom', // This line is important!
  transform: {
    '^.+\\.(ts|tsx)$': 'ts-jest',
  },
  moduleNameMapper: {
    '^./PublicWrapper$': '<rootDir>/src/PublicWrapper',
  },
};