import React, { useEffect, useState } from 'react';
import { signOut } from '../../reducks/users/operations';
import { useDispatch } from 'react-redux';
import { push } from 'connected-react-router';
import logo from '../../assets/img/logo.svg';
import cart from '../../assets/img/cart3.svg';
import person from '../../assets/img/person.svg';

function Header() {
  const dispatch = useDispatch();
  const key = localStorage.getItem('LOGIN_USER_KEY');
  const [checkUser, setCheckUser] = useState(false);

  const signOutButton = () => {
      dispatch(signOut());
      setCheckUser(false);
      dispatch(push('/signin'));
  };

  useEffect(() => {
      if (key !== null) {
          setCheckUser(true);
      }
  }, [key]);

  return (
   <>
     <header>
          <div className="logo">
            <a href="/">
              {' '}
              <img src={logo} alt="logo" />
            </a>
          </div>
          <nav>
                      {checkUser ? (
                          <span className="signin" onClick={signOutButton}>
                              Logout
                          </span>
                      ) : (
                          <a class="signin" href="Signin">
                              <img src={person} alt="user" />
                          </a>
                      )}
                      {checkUser && (
                          <a href="Cart">
                              {' '}
                              <img src={cart} alt="" />
                          </a>
                      )}
          </nav>
      </header>
   </>
  )
}

export default Header
