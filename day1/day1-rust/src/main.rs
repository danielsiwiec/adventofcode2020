fn main() {
    let content = std::fs::read_to_string("../input").expect("cannot read file");

    for line1 in content.lines() {
        for line2 in content.lines() {
            for line3 in content.lines() {
                let num1 = line1.parse::<i32>().unwrap();
                let num2 = line2.parse::<i32>().unwrap();
                let num3 = line3.parse::<i32>().unwrap();

                if num1 + num2 + num3 == 2020 {
                    println!("{}", num1*num2*num3)
                }
            }
        }
    }
}