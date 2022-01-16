from sys import stdin, stdout

class RectangleFinder():
    __raw_coordinates = list()
    __coordinates = dict()
    __is_exist = False 
    __rectangle =list()

    def __init__(self):
        pass
        
    def input_parser(self):
        try:
            lookup_coordinates = dict()
            total_coordinates = int(stdin.readline())
            
            if total_coordinates < 4:
                raise ValueError

            for i in range(total_coordinates):
                coordinate_raw = stdin.readline().split(' ')
                coordinate_int = list(map(int, coordinate_raw))
                x = coordinate_int[0]
                y = coordinate_int[1]

                x_exist = lookup_coordinates.get(x);
                if not x_exist:
                    lookup_coordinates[x] = dict()

                coordinate_exist = lookup_coordinates.get(x).get(y)
                if not coordinate_exist:
                    lookup_coordinates[x][y] = True

            for x in lookup_coordinates.keys():
                for y in lookup_coordinates.get(x).keys():
                    self.__raw_coordinates.append([x, y])
            
            del lookup_coordinates
        except ValueError:
            print("Please follow instructions in read me!")
        
    def transform_coordinates(self):
        self.__raw_coordinates = sorted(self.__raw_coordinates)
        for coordinate in self.__raw_coordinates:
            x = coordinate[0]
            y = coordinate[1]

            x_exist = self.__coordinates.get(x)
            if not x_exist:
                self.__coordinates[x] = dict()
            
            self.__coordinates[x][y] = True
            

    def solution(self):
        coordinates_size = len(self.__raw_coordinates)
        possible_vertical = list()
        if coordinates_size >= 4:
            for first_index in range(coordinates_size):
                first_coordinate = self.__raw_coordinates[first_index]

                if first_index+1 == coordinates_size:
                    break

                for second_index in range(first_index+1, coordinates_size):
                    second_coordinate = self.__raw_coordinates[second_index]
                    if second_coordinate[0] != first_coordinate[0]:
                        break
                    possible_vertical.append([first_coordinate, second_coordinate])
            
            for line in possible_vertical:
                first_y = line[0][1]
                second_y = line[1][1]
                vertical_length = abs(first_y-second_y )
                for x in self.__coordinates.keys():
                    horizontal_length = line[0][0] - x
                    if horizontal_length == vertical_length or horizontal_length == 0:
                        continue
                    
                    is_exist_point_1 = self.__coordinates.get(x).get(first_y)
                    is_exist_point_2 = self.__coordinates.get(x).get(second_y)
                    if ( is_exist_point_1 and is_exist_point_2):
                        self.__rectangle = [line[0], line[1], [x, first_y], [x, second_y]]
                        self.__is_exist = True
                        break

                if len(self.__rectangle) != 0:
                    break

        if self.__is_exist:
            print("It is possible")
            print("One of rectangle:", self.__rectangle)
        else:
            print("It is not possible")
        

    def run(self):
        self.input_parser()
        self.transform_coordinates()
        self.solution()

def main():
    rectangle_finder = RectangleFinder()
    rectangle_finder.run()

if __name__ == '__main__':
    main()