fn main() {
    let v = vec![1, 2, 3, 4, 5];
    let f = |s: Vec<i32>| {
        for i in 0..s.len() {  // тут используем v.len() напрямую
          println!("{}", &s[i]);
        };
    };
    f(v.clone());
    f(v);
}
