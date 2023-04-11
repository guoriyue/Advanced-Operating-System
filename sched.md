1. State what the point of section 5.1 is. Then state in what way Figure 3
undercuts the entire point of Section 5.1.

2. As suggested in class, you define the semantics of a volatile variable v as
giving two guarantees: (i) no additional loads or stores can be done to v
other than what appear in the program text, and (ii) an access to v cannot
be reordered with any other volatile access or lock call. Which problems
(if any) in Section 4 would this fix?

3. You see the following code below, Eraser said this “double-check lock”
idiom is broken because of memory consistency. Assume the hardware
is sequentially consistent and Boehm fixed the compiler to not be stupid
about locks. Does this code still break? Why or why not?
if ( !p ) {
    lock ( );
    if ( !p ) {
        struct foo ∗ t = foo new ( );
        t−>bar = bar new ( );
        p = t ;
    }
    unlock ( ) ;
}