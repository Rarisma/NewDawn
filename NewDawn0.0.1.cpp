// NewDawn Engine 0.0.1
// Currently working on getting the main features of the engine to accept data and getting the main loop to run
#include <windows.h>
#include <string>
#include <iostream>

int main() { //This function for now handles the main menu but in future will act as a hub for loading
  TCHAR szFilePath[_MAX_PATH];
  ::GetModuleFileName(NULL, szFilePath, _MAX_PATH);
  std::string Alt;
  Alt = szFilePath; //Stores filepath as a string from tchar

  std::cout << "NewDawn Engine Ver 0.1.0\n\n1) Play NewDawn\n2) Open Data Folder\n3) Exit\n\n" << Alt; //Displays
  int x;
  std::cin >> x;
  
  if (x == 1){ // Starts the main loop, newdawn in this case but will have a loader eventually
    std::cout << "Start Main Loop!";

  } else if (x == 2){
    system("explorer " << Alt);
  
  } else if (x == 3){ // quits program without errors
    exit(0);
  }

  return 0;
}