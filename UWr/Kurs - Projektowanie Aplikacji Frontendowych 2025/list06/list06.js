/*ZAD 1*/
console.log(capitalize("alice"));

function capitalize(str){
  return str.charAt(0).toUpperCase() + str.slice(1);
};

/*ZAD 2*/
function capitalizeSentence(sentence){
    const words = sentence.split(' ');
    const cap = words.map(capitalize);
    const result = cap.join(' ');
    return result
}

console.log(capitalizeSentence("alice"));
console.log(capitalizeSentence("alice in wonderland"));

/*ZAD 3*/
const ids = [];
/*
const generateId1 = () => {
  let id = 0;

  do {
    id++;
  } while (ids.includes(id));

  ids.push(id);
  return id;
};

console.time("generateId1");

for (let i = 0; i < 3000; i++) {
  generateId1();
}

console.timeEnd("generateId1");
*/
const ids1 = new Set();

const generateId = () => {
  let id = 0;

  do {
    id++;
  } while (ids1.has(id));

  ids1.add(id);
  return id;
};

console.time("generateId");

for (let i = 0; i < 3000; i++) {
  generateId();
}

console.timeEnd("generateId");

/*ZAD 4*/
function compareObjects(obj1, obj2){
    if (obj1 === obj2) return true;

    if (typeof obj1 !== "object" || typeof obj2 !== "object" || obj1 === null || obj2 === null) return false;

    const keys1 = Object.keys(obj1);
    const keys2 = Object.keys(obj2);

    if (keys1.length !== keys2.length) return false;

    for (let key of keys1){
        if (!obj2.hasOwnProperty(key)) return false;
        if (!compareObjects(obj1[key], obj2[key])) return false;
    }

    return true;
}

const obj1 = {
    name: "Alice",
    age: 25,
    address: {
      city: "Wonderland",
      country: "Fantasy",
    },
  };
  
const obj2 = {
    name: "Alice",
    age: 25,
    address: {
      city: "Wonderland",
      country: "Fantasy",
    },
  };
  
const obj3 = {
    age: 25,
    address: {
      city: "Wonderland",
      country: "Fantasy",
    },
    name: "Alice",
  };
  
const obj4 = {
    name: "Alice",
    age: 25,
    address: {
      city: "Not Wonderland",
      country: "Fantasy",
    },
  };
  
const obj5 = {
    name: "Alice",
  };
  
console.log("Should be True:", compareObjects(obj1, obj2));
console.log("Should be True:", compareObjects(obj1, obj3));
console.log("Should be False:", compareObjects(obj1, obj4));
console.log("Should be True:", compareObjects(obj2, obj3));
console.log("Should be False:", compareObjects(obj2, obj4));
console.log("Should be False:", compareObjects(obj3, obj4));
console.log("Should be False:", compareObjects(obj1, obj5));
console.log("Should be False:", compareObjects(obj5, obj1));

/*ZAD 5*/
let library = [];

const addBookToLibrary = (title, author, pages, isAvailable, ratings) => {
    if (title.trim() === '' || typeof title !== 'string') throw new Error("Title cannot be an empty string!");
    if (author.trim() === '' || typeof title !== 'string') throw new Error("Author cannot be an empty string!");
    if (pages <= 0 || typeof pages !== 'number') throw new Error("Pages should be a number greater than 0!");
    if (typeof isAvailable !== 'boolean') throw new Error("isAvaiable should be a boolean type!");
    if (!Array.isArray(ratings)) throw new Error("Ratings must be an array!");
    if (!ratings.every(r => typeof r === 'number' && r >= 0 && r <= 5)) throw new Error("Each rating must be a number between 0 and 5!")
    
  library.push({
    title,
    author,
    pages,
    available: isAvailable,
    ratings,
  });
};


/*ZAD 6*/
function testAddingBooks(tests){
    for (let i = 0; i < tests.length; i++){
        const {testCase, shouldFail} = tests[i];
        try{
            addBookToLibrary(...testCase);
            console.log(shouldFail? 'test failed' : 'test passed', testCase);
            /*
            if (shouldFail){
                console.log("Test " + (i + 1) + " failed");
                console.log('Test case: ', testCase);
            }
            else{
                console.log("Test " + (i + 1) + " passed");
                console.log('Test case: ', testCase);
            }
              */
        } catch (error) {
          console.log(shouldFail? 'test passed' : 'test failed', testCase, error.message);

          /*
            if (shouldFail){
                console.log("Test " + (i + 1) + " passed");
                console.log('Test case: ', testCase);
                console.log('Error message: ', error.message);
            } else {
                console.log("Test " + (i + 1) + " failed");
                console.log("Test case:", testCase);
                console.log("Error message:", error.message);
            }
                */
        }
          
    console.log('--------------------');
    }
}

const testCases = [
    { testCase: ["", "Author", 200, true, []], shouldFail: true },
    { testCase: ["Title", "", 200, true, []], shouldFail: true },
    { testCase: ["Title", "Author", -1, true, []], shouldFail: true },
    { testCase: ["Title", "Author", 200, "yes", []], shouldFail: true },
    { testCase: ["Title", "Author", 200, true, [1, 2, 3, 6]], shouldFail: true },
    {
      testCase: ["Title", "Author", 200, true, [1, 2, 3, "yes"]],
      shouldFail: true,
    },
    { testCase: ["Title", "Author", 200, true, [1, 2, 3, {}]], shouldFail: true },
    { testCase: ["Title", "Author", 200, true, []], shouldFail: false },
    { testCase: ["Title", "Author", 200, true, [1, 2, 3]], shouldFail: false },
    { testCase: ["Title", "Author", 200, true, [1, 2, 3, 4]], shouldFail: false },
    {
      testCase: ["Title", "Author", 200, true, [1, 2, 3, 4, 5]],
      shouldFail: false,
    },
    {
      testCase: ["Title", "Author", 200, true, [1, 2, 3, 4, 5]],
      shouldFail: false,
    },
  ];

console.log(testAddingBooks(testCases));

/*ZAD 7*/
function addBooksToLibrary(books){

    books.forEach(book => {
      try{addBookToLibrary(...book);

      }
      catch (error){
        console.log(error.message);
      }
        
    });
}

const books = [
    ["Alice in Wonderland", "Lewis Carroll", 200, true, [1, 2, 3]],
    ["1984", "George Orwell", 300, true, [4, 5]],
    ["The Great Gatsby", "F. Scott Fitzgerald", 150, true, [3, 4]],
    ["To Kill a Mockingbird", "Harper Lee", 250, true, [2, 3]],
    ["The Catcher in the Rye", "J.D. Salinger", 200, true, [1, 2]],
    ["The Hobbit", "J.R.R. Tolkien", 300, true, [4, 5]],
    ["Fahrenheit 451", "Ray Bradbury", 200, true, [3, 4]],
    ["Brave New World", "Aldous Huxley", 250, true, [2, 3]],
    ["The Alchemist", "Paulo Coelho", 200, true, [1, 2]],
    ["The Picture of Dorian Gray", "Oscar Wilde", 300, true, [4, 5]],
  ];

addBooksToLibrary(books);
console.log(library);