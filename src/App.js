import { Routes, Route } from 'react-router-dom';

import './App.css';

import Layout from './components/Layout/Layout';
import Home from './components/Home/Home';
import SimMain from './components/SimMain/SimMain';
import Names from './components/Names/Names';

const App = () => {
	return (
		<>
			<Routes>
				<Route path='/' element={<Layout />}>
					<Route path='/' element={<Home />}>
						<Route path='/generate-sim' element={<SimMain />} />
						<Route path='/generate-name' element={<Names />} />
					</Route>
				</Route>
			</Routes>
		</>
	);
};
export default App;
