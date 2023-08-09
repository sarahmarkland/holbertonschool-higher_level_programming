#!/usr/bin/node
exports.converter = function (base) {
  return function convertToBase (num) {
    return num.toString(base);
  };
};
